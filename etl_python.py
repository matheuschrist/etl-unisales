# -*- coding: utf-8 -*-
"""ETL-python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/108CoptNjIJEOmx4A5LGW6NeUdRknO5_Z
"""

from google.colab import drive
drive.mount('/content/drive')

"""#Extração dos dados"""

import pandas as pd




olist_customers = '/content/drive/MyDrive/Colab Notebooks/dados/olist_customers_dataset.csv' 
olist_order_items_dataset='/content/drive/MyDrive/Colab Notebooks/dados/olist_order_items_dataset.csv'
olist_order_payments_dataset='/content/drive/MyDrive/Colab Notebooks/dados/olist_order_payments_dataset.csv'
olist_orders_dataset='//content/drive/MyDrive/Colab Notebooks/dados/olist_orders_dataset.csv'
olist_sellers_dataset='/content/drive/MyDrive/Colab Notebooks/dados/olist_sellers_dataset.csv'



customers = pd.read_csv(olist_customers)
order_items=pd.read_csv(olist_order_items_dataset)
payments=pd.read_csv(olist_order_payments_dataset)
orders=pd.read_csv(olist_orders_dataset)
sallers=pd.read_csv(olist_sellers_dataset)

#Excluindo as colunas da tabela de pedidos  que não serão utilizadas 
orders.drop(labels=['order_purchase_timestamp','order_delivered_carrier_date','order_delivered_customer_date','order_estimated_delivery_date'], axis=1,inplace=True)

#Excluindo as colunas da tabela de pagamentos  que não serão utilizadas 
payments.drop(labels=['payment_sequential','payment_installments'], axis=1,inplace=True)

#Excluindo as colunas da tabela de itens  que não serão utilizadas 
order_items.drop(labels=['shipping_limit_date'], axis=1,inplace=True)

#Excluindo as colunas da tabela de clientes  que não serão utilizadas 
customers.drop(['customer_unique_id'], axis=1,inplace=True)

#Excluindo as colunas da tabela de vendedores que não serão utilizadas
#sallers.drop(['seller_city','seller_state'], axis=1,inplace=True)

#Excluindo as colunas da tabela de Localização que não serão utilizadas 
#geolocation.drop(['geolocation_lat','geolocation_lng'], axis=1,inplace=True)

"""#Criando a Tabela calendário"""

import pandas as pd

def create_date_table(start='1980-01-01', end='2021-12-31'):
    start_ts = pd.to_datetime(start).date()

    end_ts = pd.to_datetime(end).date()

  
    dates =  pd.DataFrame(index=pd.date_range(start_ts, end_ts))
    dates.index.name = 'Date'

    days_names = {
        i:name
        for i, name in enumerate(['Domingo', 'Segunda-feria', 'Terça-feira',
                      'Quarta-Feira', 'Quinta-feria', 'Sexta-feira', 
                      'Sabado'])
    }
    
    dates['DiaSemana'] = dates.index.dayofweek.map(days_names.get)
    dates['Dia'] = dates.index.day
    dates['Semana'] = dates.index.week
    dates['Mês'] = dates.index.month
    dates['Trimestre'] = dates.index.quarter
    dates['Semestre'] = dates.index.month.map(lambda mth: 1 if mth <7 else 2)
    dates['Ano'] = dates.index.year
    dates['date_id'] = dates['Dia'].astype(str)+dates['Mês'].astype(str)+dates['Ano'].astype(str)
    dates.reset_index(inplace=True)
    

    #print(len(dates))
    #print(dates.head(5))
    
      

    return dates




create_date_table()

"""#Transoformação a data para o mesmo padrão da tabela calendário"""

import math
orders['Dia'] = pd.DatetimeIndex(orders['order_approved_at']).day
orders['Mês'] = pd.DatetimeIndex(orders['order_approved_at']).month
orders['Ano'] = pd.DatetimeIndex(orders['order_approved_at']).year

#convertendo as datas para int
for mes in orders['Mês']:
#Verifica se possui valores vazios e adiciona zero caso for Verdadeiro
  if math.isnan(mes) == True:
    orders['Mês']=0
  else:
    orders['Mês']=int(mes)
for dia in orders['Dia']:
  if math.isnan(dia) == True:
    orders['Dia']=0
  else:
    orders['Dia']=int(dia)
for ano in orders['Ano']:
  if math.isnan(ano) == True:
    orders['Ano']=0
  else:
    orders['Ano']=int(ano)




orders['order_approved_at']= orders['Dia'].astype(str)+orders['Mês'].astype(str)+orders['Ano'].astype(str)

#Criando a tabela Fato 
#Verificar o melhor parametro
orders=orders.rename(columns={'order_approved_at': 'data_id'})
fato_orders = pd.merge(orders,payments, how = 'left',on='order_id')
fato_orders= pd.merge(fato_orders,order_items, how = 'left', on = 'order_id')




display(fato_orders)

"""#Carregamento no DW

#Criando as tabelas no banco de dados
"""



from sqlalchemy import create_engine



#Cria a conexão com o DB
engine = create_engine('postgresql://dbaadmin:Batatinha##2022@dw-unisales-dados.postgres.database.azure.com/postgres')
#postgres://dbaadmin:{your_password}@dw-unisales-dados.postgres.database.azure.com/postgres?sslmode=require
conn = engine.connect()
print("Connection established")

if False:
  #insere os dados da DataFrame no banco de dados 
  fato_orders.to_sql(name='fato_orders' , con=conn , schema = None , if_exists = 'replace' , index = True , index_label = None ,
                    chunksize = None , dtype = None , method = None )
  customers.to_sql(name='customers' , con=conn , schema = None , if_exists = 'replace' , index = True , index_label = None ,
                    chunksize = None , dtype = None , method = None )
  sallers.to_sql(name='sallers' , con=conn , schema = None , if_exists = 'replace' , index = True , index_label = None ,
                    chunksize = None , dtype = None , method = None )
  geolocation.to_sql(name='geolocation' , con=conn , schema = None , if_exists = 'replace' , index = True , index_label = None ,
                    chunksize = None , dtype = None , method = None )