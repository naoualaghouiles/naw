"""isEmpty methode"""


class PizzaCarte:
    """isEmpty methode"""
    def __init__(self, pizza= None) :
        """constructeur"""
        self.__pizza=pizza

    @property
    def pizza(self):
        """The pizza property."""
        return self.__pizza
    @pizza.setter
    def pizza(self, value):
        """setter"""
        self.__pizza = value

    def is_empty(self):
        """isEmpty methode"""
        return not self.__pizza

    def nombre(self):
        """isEmpty methode"""
        return len(self.pizza)


    def add_pizza(self, pizza) :
        """isEmpty methode"""
        self.__pizza.append(pizza)

    def remove_pizza(self, pizza):
        """isEmpty methode"""
        try:
            self.__pizza.remove(pizza)
        except ValueError:
            Exception("Pizza not found")

# if __name__ == "__main__":
#     p= PizzaCarte()
#     p.pizza=[1,2,3]
#     print(p.is_empty())
#     print(p.nombre())
    