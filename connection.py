
from sqlalchemy import create_engine

def conection_dw():
    #Carregamento no DW"""
    engine = create_engine('sqlite:///:memory:', echo=True)       
    #('postgresql://dbaadmin:{senha}@dw-unisales-dados.postgres.database.azure.com:5432/postgres')   
    #('sqlite:///:memory:', echo=True 
    conn=engine.connect()
    print("Connection established")


    return engine,conn

