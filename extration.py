

import pandas as pd


"""#Extração dos dados"""

def extracao_dados():
        
    olist_customers = 'base_dados/olist_customers_dataset.csv' 
    olist_order_items_dataset='base_dados/olist_order_items_dataset.csv'
    olist_order_payments_dataset='base_dados/olist_order_payments_dataset.csv'
    olist_orders_dataset='base_dados/olist_orders_dataset.csv'
    olist_sellers_dataset='base_dados/olist_sellers_dataset.csv'



    customers = pd.read_csv(olist_customers)
    order_items=pd.read_csv(olist_order_items_dataset)
    payments=pd.read_csv(olist_order_payments_dataset)
    orders=pd.read_csv(olist_orders_dataset)
    sallers=pd.read_csv(olist_sellers_dataset)
    
    
    
    
   
    
    return customers,order_items,payments,orders,sallers




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
    
    
      

    return dates






