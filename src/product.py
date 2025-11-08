from typing import Union
class Product:
    def __init__(self,name : str, value : Union[int, float] ):
        self.__name = name
        self.__value = value
    @property
    def name(self) -> str: 
        return self.__name
    
    @property
    def price(self)-> float:
        return self.__value
    
    @price.setter
    def price(self,value):
        if value<0:
            raise ValueError("value cannot be negative")
        self.__value = value
    
    @name.setter
    def name(self, name):
        if  not name:
            raise ValueError("name cannot be null")
        self.__name = name
         
    