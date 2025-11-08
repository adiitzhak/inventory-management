import pytest
from src.product import Product


def test_name(chair_product, book_product):
    """testing for constructor initialzation"""
    assert chair_product.name == "chair"
    chair_product.name = 123
    assert chair_product.name == 123
    chair_product.name ="book"
    assert chair_product.name =="book"
    with pytest.raises(ValueError):
        chair_product.name=""
    
def test_value(chair_product, book_product):
    """testing if value"""
    assert chair_product.price == 10
    with pytest.raises(ValueError):
        chair_product.price = -1
        

        