

import pandas as pd

from tabelas import Products


"""#Extração dos dados"""

def extracao_dados():
        
    olist_customers = 'base_dados/olist_customers_dataset.csv' 
    olist_order_items_dataset='base_dados/olist_order_items_dataset.csv'
    olist_order_payments_dataset='base_dados/olist_order_payments_dataset.csv'
    olist_orders_dataset='base_dados/olist_orders_dataset.csv'
    olist_sellers_dataset='base_dados/olist_sellers_dataset.csv'
    olist_products_dataset='base_dados/olist_products_dataset.csv'



    customers = pd.read_csv(olist_customers)
    order_items=pd.read_csv(olist_order_items_dataset)
    payments=pd.read_csv(olist_order_payments_dataset)
    orders=pd.read_csv(olist_orders_dataset)
    sellers=pd.read_csv(olist_sellers_dataset)
    products=pd.read_csv(olist_products_dataset)
    
    
    print("Feito a extração dos dados")
    
   
    
    return customers,order_items,payments,orders,sellers,products





def create_date_table(start='2000-01-01', end='2022-12-31'):
    start_ts = pd.to_datetime(start).date()

    end_ts = pd.to_datetime(end).date()

  
    dates =  pd.DataFrame(index=pd.date_range(start_ts, end_ts))
    dates.index.name = 'date'

    days_names = {
        i:name
        for i, name in enumerate(['Domingo', 'Segunda-feria', 'Terça-feira',
                      'Quarta-Feira', 'Quinta-feria', 'Sexta-feira', 
                      'Sabado'])
    }
    
    dates['dayweek'] = dates.index.dayofweek.map(days_names.get)
    dates['day'] = dates.index.day
    dates['week'] = dates.index.isocalendar().week
    dates['month'] = dates.index.month
    dates['quarter'] = dates.index.quarter
    dates['semester'] = dates.index.month.map(lambda mth: 1 if mth <7 else 2)
    dates['year'] = dates.index.year
    dates['date_id'] = dates['day'].astype(str)+'-'+dates['month'].astype(str)+'-'+dates['year'].astype(str)
    dates.reset_index(inplace=True)

        
    
    print("Tabela tempo Criada")

    return dates




