import pytest
from src.inventory import Inventory
from src.product import Product


@pytest.fixture
def inventory():
    """fixture inventory"""
    return Inventory()
def test_inventory(inventory):
    assert inventory.products == {}

def test_add_product(inventory,chair_product, book_product):
    """testing after product adding the product exists """
    inventory.add_product(chair_product)
    inventory.add_product(chair_product)
    inventory.add_product(book_product)
    assert inventory.products[chair_product] == 2
    assert inventory.products[book_product]==1
    
def test_remove_product(inventory, chair_product, book_product):
    """testing after product remove from inventory"""
    
    inventory.add_product(chair_product)
    inventory.add_product(chair_product)
    inventory.remove_product(chair_product.name)
    assert inventory.products[chair_product] == 1
    inventory.remove_product(chair_product.name)
    assert chair_product not in inventory.products.keys()
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
    assert inventory.total_inventory_price() == 35.0
    

