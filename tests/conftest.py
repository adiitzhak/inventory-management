##contest.py
import pytest
from src.product import Product

 #product fixture -> Chair, Book   
@pytest.fixture
def chair_product():
    return Product("chair",10)
    
@pytest.fixture
def book_product():
    return Product("book", 15)

