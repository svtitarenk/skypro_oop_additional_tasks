from abc import ABC, abstractmethod

class BaseProduct(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass

    @abstractmethod
    def __str__(self):
        pass

class PrintMixin:

    def __init__(self):
        print(str(self))

    def __str__(self):
        pass

class Product(BaseProduct, PrintMixin):
    """
    Класс для описания товара в магазине
    """
    category_count = 0
    product_count = 0

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()
        print(repr(self))

    @classmethod
    def new_product(cls, product):
        return cls(product["name"], product["description"], product["price"], product["quantity"])

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print('Цена не должна быть нулевая или отрицательная')
        else:
            self.__price = new_price

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.__price}, {self.quantity})"

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("Нельзя складывать товары разных классов")
        return (self.__price * self.quantity) + (other.__price * other.quantity)

    def __eq__(self, other):
        if isinstance(other, Product):
            return self.name == other.name
        return False


class Category:
    """
    Класс для категорий товара
    """
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    @property
    def products(self):
        return self.__products

    @products.setter
    def products(self, prod: Product):
        if isinstance(prod, Product):
            self.__products.append(prod.name)
        else:
            raise TypeError

    def __str__(self):
        return f'{self.name}, количество продуктов: {sum([product.quantity for product in self.__products])} шт.'


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        return f"Smartphone('{self.name}', '{self.description}', {self.price}, {self.quantity})"

class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        return f"LawnGrass('{self.name}', '{self.description}', {self.price}, {self.quantity})"