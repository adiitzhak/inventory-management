from typing import Union
class Product:
    def __init__(self,name : str, price : Union[int, float] ):
        self.__name = name
        self.__price = price
        
    @property
    def name(self) -> str: 
        return self.__name
    
    @property
    def price(self)-> float:
        return self.__price
    
    @price.setter
    def price(self,price):
        if price<0:
            raise ValueError("value cannot be negative")
        self.__price = price
    
    @name.setter
    def name(self, name):
        if  not name:
            raise ValueError("name cannot be null")
        self.__name = name
         
    