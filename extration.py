

import pandas as pd


"""#Extração dos dados"""

def extracao_dados():
        
    olist_customers = 'base_dados/olist_customers_dataset.csv' 
    olist_geolocation_dataset='base_dados/olist_geolocation_dataset.csv'
    olist_order_items_dataset='base_dados/olist_order_items_dataset.csv'
    olist_order_payments_dataset='base_dados/olist_order_payments_dataset.csv'
    olist_orders_dataset='base_dados/olist_orders_dataset.csv'
    olist_sellers_dataset='base_dados/olist_sellers_dataset.csv'



    customers = pd.read_csv(olist_customers)
    geolocation=pd.read_csv(olist_geolocation_dataset)
    order_items=pd.read_csv(olist_order_items_dataset)
    payments=pd.read_csv(olist_order_payments_dataset)
    orders=pd.read_csv(olist_orders_dataset)
    sallers=pd.read_csv(olist_sellers_dataset)
   
    
    return customers,geolocation,order_items,payments,orders,sallers



