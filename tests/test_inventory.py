import pytest
from src.inventory import Inventory
from src.database.database import Database
 
@pytest.fixture
def inventory():
        """fixture inventory"""
        db_client = Database()
        db_client.collection = db_client.db["test_products"]
        inv = Inventory()
        inv.database = db_client
        yield inv  
        db_client.collection.delete_many({})



def test_add_product(inventory, chair_product, book_product):
        """testing after product adding the product exists """
        inventory.add_product(chair_product)
        inventory.add_product(chair_product)
        inventory.add_product(book_product)
        chair =  inventory.database.collection.find_one({"name" : chair_product.name} ) 
        assert chair["quantity"] == 2
        book =  inventory.database.collection.find_one({"name" : book_product.name} ) 
        assert book["quantity"] == 1 
        
def test_remove_product(inventory, chair_product, book_product):
        """testing after product remove from inventory"""
        inventory.add_product(chair_product)
        inventory.add_product(chair_product)
        inventory.remove_product(chair_product.name)
        chair = inventory.database.collection.find_one({"name":chair_product.name })
        assert chair["quantity"] == 1
        inventory.remove_product(chair_product.name)
        if_found = inventory.database.collection.find_one({"name" : chair_product.name})
        assert if_found is None
        with pytest.raises(ValueError):
            inventory.remove_product(book_product.name)
            
def test_get_product(inventory, chair_product, book_product):
        """testing if product exists return product by name"""
        inventory.add_product(chair_product)    
        assert inventory.get_product(chair_product.name)
        with pytest.raises(ValueError):
            inventory.get_product(book_product.name)
        
def test_total_price(inventory, chair_product, book_product):
        """testing for calculate is true"""  
        inventory.add_product(chair_product)
        inventory.add_product(chair_product)  
        inventory.add_product(book_product)  
        chair_in_db = inventory.database.collection.find_one({"name": chair_product.name})
        book_in_db = inventory.database.collection.find_one({"name" : book_product.name})
        assert chair_in_db is not None
        assert chair_in_db["quantity"] == 2
        assert book_in_db  is not None
        assert book_in_db["quantity"] ==1
        assert inventory.total_inventory_price() == 35.0
        

