from sqlalchemy import create_engine    
import pandas as pd 
import os

os.system('cls')

host = 'localHost'
user = 'root'
password = ''
database = 'bd_atividade02'

engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')


try: 
    df_clientes = pd.read_sql('tb_clientes', engine)
    df_itens = pd.read_sql('tb_itens', engine)
    df_pedidos = pd.read_sql('tb_pedidos', engine)
    df_produtos = pd.read_sql('tb_produtos', engine)
except Exception as e: 
    print(f'Erro na conexão {e}')



try: 
    df_merge1 = pd.merge(df_itens, df_produtos, on='codigo_produto')
    df_merge2 = pd.merge(df_merge1, df_pedidos, on='codigo_pedido')
    df_final = pd.merge(df_merge2, df_clientes, on='codigo_cliente')

    filtros = df_final['cidade'] == 'Sao Paulo'

    df_SaoPaulo = df_final[filtros]

    print(df_SaoPaulo[[
        'nome',
        'sobrenome',
        'cidade',
        'codigo_pedido',
        'data_pedido',
        'produto',
        'valor'
                    ]])
    
except Exception as e:
    print(f'Erro no tratamento dos dados {e}')


    # ==============================================================================


    # juntar dois dataframes com campos exatamentes iguais.
    # df_merge1 = pd.merge(df_itens, df_produtos, on='codigo_produto')

    # juntar dois dataframes com campos diferentes.
    # df_merge1 = pd.merge(
    #     df_itens, 
    #     df_produtos, 
    #     left_on='codigo_produto'
    #     right_on='cliente_codigo'
    # )