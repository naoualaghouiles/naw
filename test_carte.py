"""isEmpty methode"""
from unittest.mock import Mock
from carte_pizza import PizzaCarte


def test_is_empty():
    """isEmpty methode"""
    carte= PizzaCarte()
    carte.pizza=[]
    assert carte.is_empty()


def test_nombre():
    """isEmpty methode"""
    carte= PizzaCarte()
    carte.pizza=[1,4,5,6]
    assert carte.nombre()==4

def test_add_pizza() :
    """isEmpty methode"""
    pizza=Mock()
    carte= PizzaCarte()
    carte.pizza=[]
    carte.add_pizza(pizza)

    assert carte.pizza==[pizza]


def test_remove_pizza():
    """isEmpty methode"""
    pizza=Mock()
    carte= PizzaCarte()
    carte.pizza=[pizza]

    carte.remove_pizza(pizza)
    assert not carte.pizza
    