from src.product import Product
from src.database.database import Database

class Inventory:
    def __init__(self):
        """init null directionary"""
        self.__products = {}
        self.database = Database()
        
    @property
    def products(self):
        """get products from directionary"""
        return self.__products
          
    def add_product(self,product : Product):
        """ add product to products"""
        if product in self.__products.keys():
            self.__products[product] += 1
        else:
            self.__products[product] = 1
            
        
        
    def remove_product(self, product_name : str) -> None:
        """remove product from dictionary"""
        for item in self.__products.keys():
             if item.name == product_name:
                self.__products[item] -= 1
                if self.__products[item] == 0:
                    del self.__products[item]
                return
        raise ValueError("we can't found this product :(")
       
     
    def get_product(self, product_name : str) ->Product:
        """return product by name"""
        for product in self.__products.keys():
             if product.name == product_name:
                 return product
             raise ValueError("we can't found this product")
        return None

         
    def total_inventory_price(self) -> float:
        """calculate total price"""
        total_price = 0.0
        for product, count in self.__products.items():
            total_price += product.price * count
        return total_price
            
           
        
        
        
                
            
        
   
        
        
        
        
        
 
        