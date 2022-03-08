from hashlib import new
from pickle import APPEND


class PizzaCarte:
    def __init__(self, pizza=[]) :
        self.__pizza=pizza
    
    @property
    def pizza(self):
        """The pizza property."""
        return self.__pizza
    @pizza.setter
    def pizza(self, value):
        self.__pizza = value
        
    def is_empty(self):
        return not self.__pizza
    
    def nombre(self):
        return len(self.pizza)
     
        
    def add_pizza(self, pizza) :
        self.__pizza.append(pizza)
        
        
    def remove_pizza(self, pizza):
        try:
            self.__pizza.remove(pizza)
        except ValueError:
            Exception("Pizza not found")
    
if __name__ == "__main__":
    p= PizzaCarte()
    p.pizza=[1,2,3]
    print(p.is_empty())
    
    print(p.nombre())
    
    
        
        