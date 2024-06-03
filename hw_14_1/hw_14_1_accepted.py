class Product:
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

        Product.category_count += 1
        Product.product_count += 1

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

    def __str__(self):
        return f'{self.name}, {int(self.price)} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
       return (self.__price * self.quantity) + (other.__price * other.quantity)

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
    def product(self):
        return self.__products

    @product.setter
    def product(self, product):
        self.__products.append(product)

    @property
    def products(self):
        return self.__products

    def __str__(self):
        return f'{self.name}, количество продуктов: {sum([product.quantity for product in self.__products])} шт.'