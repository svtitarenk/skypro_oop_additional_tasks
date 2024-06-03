from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """ базовый абстрактный класс """

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass


class MixinProduct:

    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.price}, {self.quantity})"


class Product(BaseProduct, MixinProduct):
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


data = [
    {
        "name": "Смартфоны",
        "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
        "products": [
            {
                "name": "Samsung Galaxy C23 Ultra",
                "description": "256GB, Серый цвет, 200MP камера",
                "price": 180000.0,
                "quantity": 5
            },
            {
                "name": "Iphone 15",
                "description": "512GB, Gray space",
                "price": 210000.0,
                "quantity": 8
            },
            {
                "name": "Xiaomi Redmi Note 11",
                "description": "1024GB, Синий",
                "price": 31000.0,
                "quantity": 14
            }
        ]
    },
    {
        "name": "Телевизоры",
        "description": "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        "products": [
            {
                "name": "55 QLED 4K",
                "description": "Фоновая подсветка",
                "price": 123000.0,
                "quantity": 7
            }
        ]
    }
]

class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

""" test 1 """

# categories = []
# for category in data:
#     products = []
#     for product in category['products']:
#         products.append(Product.new_product(product))  # добавленный метод
#     category['products'] = products
#     categories.append(Category(**category))
#
# product_item = Product('Test', 'Test', 1000, 10)
# product_item_2 = Smartphone('Test2', 'Test2', 2000, 10, 1.5, 'Xiaomi', 10000, 'red')
# product_item_3 = LawnGrass('Test3', 'Test3', 3000, 10, 'Canada', '1 year', 'light green')
#
# try:
#     broken_product = Product('Test', 'Test', 1000, 0)
# except ValueError as e:
#     print( str(e) == "Товар с нулевым количеством не может быть добавлен")

"""
Ожидаемый ответ:

Product('Samsung Galaxy C23 Ultra', '256GB, Серый цвет, 200MP камера', 180000.0, 5)
Product('Iphone 15', '512GB, Gray space', 210000.0, 8)
Product('Xiaomi Redmi Note 11', '1024GB, Синий', 31000.0, 14)
Product('55 QLED 4K', 'Фоновая подсветка', 123000.0, 7)
Product('Test', 'Test', 1000, 10)
Smartphone('Test2', 'Test2', 2000, 10)
LawnGrass('Test3', 'Test3', 3000, 10)
True
"""


""" test 2 """

# categories = []
# for category in data:
#     products = []
#     for product in category['products']:
#         products.append(Product.new_product(product))  # добавленный метод
#     category['products'] = products
#     categories.append(Category(**category))
#
# product_item = Product('Test', 'Test', 1000, 10)
# product_item_2 = Smartphone('Test2', 'Test2', 2000, 10, 1.5, 'Xiaomi', 10000, 'red')
# product_item_3 = LawnGrass('Test3', 'Test3', 3000, 10, 'Canada', '1 year', 'light green')
#
#
#
# print( categories[0].middle_price() == 140333.33333333334)

"""

Ожидаемый ответ:

Product('Samsung Galaxy C23 Ultra', '256GB, Серый цвет, 200MP камера', 180000.0, 5)
Product('Iphone 15', '512GB, Gray space', 210000.0, 8)
Product('Xiaomi Redmi Note 11', '1024GB, Синий', 31000.0, 14)
Product('55 QLED 4K', 'Фоновая подсветка', 123000.0, 7)
Product('Test', 'Test', 1000, 10)
Smartphone('Test2', 'Test2', 2000, 10)
LawnGrass('Test3', 'Test3', 3000, 10)
True

"""


""" test 3 """

# categories = []
# for category in data:
#     products = []
#     for product in category['products']:
#         products.append(Product.new_product(product))  # добавленный метод
#     category['products'] = products
#     categories.append(Category(**category))
#
# product_item = Product('Test', 'Test', 1000, 10)
# product_item_2 = Smartphone('Test2', 'Test2', 2000, 10, 1.5, 'Xiaomi', 10000, 'red')
# product_item_3 = LawnGrass('Test3', 'Test3', 3000, 10, 'Canada', '1 year', 'light green')
#
#
# null_category = Category('Test', 'Test', [])
#
# print( null_category.middle_price() == 0)

"""
Ожидаемый ответ:

Product('Samsung Galaxy C23 Ultra', '256GB, Серый цвет, 200MP камера', 180000.0, 5)
Product('Iphone 15', '512GB, Gray space', 210000.0, 8)
Product('Xiaomi Redmi Note 11', '1024GB, Синий', 31000.0, 14)
Product('55 QLED 4K', 'Фоновая подсветка', 123000.0, 7)
Product('Test', 'Test', 1000, 10)
Smartphone('Test2', 'Test2', 2000, 10)
LawnGrass('Test3', 'Test3', 3000, 10)
True
"""