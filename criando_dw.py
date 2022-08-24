

from transformacao import transformation as trans

from sqlalchemy import create_engine

#Carregamento no DW"""
fato_orders,sallers,customers,geolocation=trans()


engine = create_engine(
    'postgresql://dbaadmin:{senha}@dw-unisales-dados.postgres.database.azure.com:5432/postgres')
conn=engine.connect()
print("Connection established")

#insere os dados da DataFrame no banco de dados 
fato_orders.to_sql(name='fato_orders' , con=conn , schema = None , if_exists = 'replace' , index = True , index_label = None ,
                   chunksize = None , dtype = None , method = None )
print('Executado')
customers.to_sql(name='customers' , con=conn , schema = None , if_exists = 'replace' , index = True , index_label = None ,
                   chunksize = None , dtype = None , method = None )
print('Executado')
sallers.to_sql(name='sallers' , con=conn , schema = None , if_exists = 'replace' , index = True , index_label = None ,
                   chunksize = None , dtype = None , method = None )
print('Executado')
geolocation.to_sql(name='geolocation' , con=conn , schema = None , if_exists = 'replace' , index = True , index_label = None ,
                   chunksize = None , dtype = None , method = None )
print('Executado')