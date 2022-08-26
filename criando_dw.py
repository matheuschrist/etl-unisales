
from connection import conection_dw as connection
from tabelas import Base as base
from transformacao import transformation



def criando_dw():
    
    fato_orders,sellers,customers,products,date=transformation()
    
    engine,conn=connection()

    #Inserindo as mudanças no banco -Criando as tabelas
    base.metadata.create_all(engine)


    
    #insere os dados da DataFrame no banco de dados 
   
    customers.to_sql(name='dimension_customers' , con=conn , schema = None , if_exists = 'append' , index = None , index_label = None ,
                    chunksize = None , dtype = None , method = None )
    print('Executado')
    sellers.to_sql(name='dimension_sellers' , con=conn , schema = None , if_exists = 'append' , index = None , index_label = None ,
                    chunksize = None , dtype = None , method = None )
    print('Executado')
    date.to_sql(name='dimension_date' , con=conn , schema = None , if_exists = 'append' , index = None , index_label = None ,
                    chunksize = None, dtype = None , method = None )
    print('Executado')
    products.to_sql(name='dimension_products' , con=conn , schema = None , if_exists = 'append' , index = None , index_label = None ,
                    chunksize = None , dtype = None , method = None )
    print('Executado')
    fato_orders.to_sql(name='fact_orders' , con=conn , schema = None , if_exists = 'append' , index = None , index_label = None ,
                    chunksize = None , dtype = None , method = None )
     
    print('Executado')

    



criando_dw()