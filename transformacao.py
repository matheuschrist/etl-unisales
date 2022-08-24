import pandas as pd
from extration import extracao_dados as ex
import math




def transformation():
    """#Transoformação dos dados """


    customers,order_items,payments,orders,sallers=ex()
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



        
    """#Transoformação a data para o mesmo padrão da tabela calendário"""

    
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



    return fato_orders,sallers,customers


