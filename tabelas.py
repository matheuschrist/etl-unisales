
from enum import unique
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String , DateTime,Float,ForeignKey 
from sqlalchemy import UniqueConstraint




Base = declarative_base()


class Products(Base):
    __tablename__ = 'dimension_products'

    product_id = Column(String, primary_key=True)
    product_name_lenght = Column(String)
    product_category_name = Column(String)

   
    
class Date(Base):
    __tablename__='dimension_date'
    date_id=Column(String, primary_key=True)
    day=Column(Integer)
    week=Column(Integer)
    dayweek=Column(String)
    month=Column(Integer)
    quarter=Column(Integer)
    semester=Column(Integer)
    year=Column(Integer)
    date=Column(DateTime)


class Customers(Base):
    __tablename__='dimension_customers'
    
    customer_id=Column(String, primary_key=True)
    customer_zip_code_prefix=Column(String)
    customer_city=Column(String)
    customer_state=Column(String)
    
    


class Sellers(Base):
    __tablename__='dimension_sellers'
    seller_id=Column(String, primary_key=True)
    seller_zip_code_prefix=Column(String)
    seller_city=Column(String)
    seller_state=Column(String)
    
    
    
class Orders(Base):
    __tablename__='fact_orders'
    
    order_id=Column(String, primary_key=True )
    order_item_id=Column(String, primary_key=True)
    customer_id=Column(String, ForeignKey('dimension_customers.customer_id'))
    seller_id=Column(String, ForeignKey('dimension_sellers.seller_id'))
    date_id=Column(String, ForeignKey('dimension_date.date_id'))
    product_id = Column(String, ForeignKey('dimension_products.product_id'))
    order_status=Column(String)
    price=Column(Float)
    freight_value=Column(Float)
    payment_value=Column(Float)
    payment_type=Column(String)
    Dia=Column(Integer)
    Mês=Column(Integer)
    Ano=Column(Integer)
    
    
    
    
    
    