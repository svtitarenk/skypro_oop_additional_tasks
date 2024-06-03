"""
Для класса Category сделайте список товаров приватным атрибутом,
чтобы к нему нельзя было получить доступ извне.

Для добавления товаров в категорию реализуйте специальный метод,
в который нужно передавать объект класса Product и уже его записывать
в приватный атрибут списка товаров.

Так как вы сделали атрибут со списком товаров приватным, то
атрибут «список товаров категории» у вас освободился,
но вы лишили программу возможности выводить список товаров.
Чтобы вернуть возможность просмотра товаров, нужно реализовать геттер,
который будет выводить список товаров в виде строк в формате:

Название продукта, 80 руб. Остаток: 15 шт.

Для класса Product необходимо создать класс-метод new_product,
который будет принимать на вход параметры товара и возвращать созданный объект класса Product.

Для класса Product сделайте атрибут цены приватным и
опишите геттеры и сеттеры. В сеттере реализуйте проверку:
в случае если цена равна или ниже нуля, выводите сообщение в консоль
“Цена не должна быть нулевая или отрицательная”,
при этом новую цену устанавливать не нужно.

"""


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
        return f'{self.__price}'

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print('Цена не должна быть нулевая или отрицательная')
        else:
            self.__price = new_price


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
    def products(self) -> str:
        products_str = ''
        for product in self.__products:
            products_str += f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n'
        return products_str



""" проверка через тесты на Скайпро """


def check_homework():
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

    categories = []
    for category in data:
        products = []
        print('category', category)
        for product in category['products']:
            print('product', product)
            products.append(Product.new_product(product))
        category['products'] = products
        print("category['products']", category['products'])
        categories.append(Category(**category))

    print('product_item.__dict__', Product.new_product)
    # print('product_item.__dict__', Category.__dict__)
    assert categories[0].products == """Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.
    Iphone 15, 210000.0 руб. Остаток: 8 шт.
    Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.
    """

    product_item = Product('Test', 'Test', 1000, 10)
    print('product_item.__dict__', product_item.__dict__)
    print(product_item.price)

    product_item.price = 800
    print(product_item.price)



if __name__ == '__main__':
    check_homework()

