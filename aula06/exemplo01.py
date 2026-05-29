from sqlalchemy import create_engine    
import pandas as pd
import os   

os.system('cls')

host = 'localHost'
user = 'root'
password = ''
database = 'bd_biblioteca'

engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')


try:
    df_usuarios = pd.read_sql('tb_usuarios', engine)
    df_itens_alugados = pd.read_sql('tb_itens_alugados', engine)
    df_livros = pd.read_sql('tb_livros', engine)
    df_alugados = pd.read_sql('tb_alugados', engine)
except Exception as e:
    print(f'Falha na conexão {e}')

# print(df_usuarios.head())
# print(df_itens_alugados.head())
# print(df_livros.head())
# print(df_alugados.head())

# Juntando os Dataframes

try:
    df_merge1 = pd.merge(df_livros, df_itens_alugados, on='id_livro')
    df_merge2 = pd.merge(df_merge1, df_alugados, on='id_aluguel')
    df_final = pd.merge(df_merge2, df_usuarios, on='id_usuario')
    #print(df_final)
    
    filtros = (
        (df_final['data_devolucao'] >= '2024-11-01') &
        (df_final['data_devolucao'] <= '2024-11-30')
        )
    
    df_novembro = df_final[filtros]

    print(
        df_novembro[[
            'id_usuario',
            'nome',
            'id_aluguel',
            'data_aluguel',
            'data_devolucao', 
            'valor',
            'id_livro', 'titulo'

        ]]
        )

except Exception as e:
    print(f'Erro tratamento dos dados {e}')



