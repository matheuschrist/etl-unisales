import pandas as pd
from extration import extracao_dados as ex




def transformation():
    """#Transoformação dos dados """


    customers,geolocation,order_items,payments,orders,sallers=ex()
    #Excluindo as colunas da tabela de pedidos  que não serão utilizadas 
    orders.drop(labels=['order_purchase_timestamp','order_delivered_carrier_date','order_delivered_customer_date','order_estimated_delivery_date'], axis=1,inplace=True)

    #Excluindo as colunas da tabela de pagamentos  que não serão utilizadas 
    payments.drop(labels=['payment_sequential','payment_installments'], axis=1,inplace=True)

    #Excluindo as colunas da tabela de itens  que não serão utilizadas 
    order_items.drop(labels=['shipping_limit_date'], axis=1,inplace=True)

    #Excluindo as colunas da tabela de clientes  que não serão utilizadas 
    customers.drop(['customer_unique_id','customer_city','customer_state'], axis=1,inplace=True)

    #Excluindo as colunas da tabela de vendedores que não serão utilizadas 

    sallers.drop(['seller_city','seller_state'], axis=1,inplace=True)

    #Excluindo as colunas da tabela de Localização que não serão utilizadas 
    geolocation.drop(['geolocation_lat','geolocation_lng'], axis=1,inplace=True)



    #Criando a tabela Fato 
    fato_orders = pd.merge(payments, orders, how = 'inner', on = 'order_id')
    fato_orders= pd.merge(order_items, fato_orders, how = 'inner', on = 'order_id')


    return fato_orders,sallers,customers,geolocation


