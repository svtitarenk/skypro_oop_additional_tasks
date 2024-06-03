import warnings

warnings.filterwarnings('ignore')


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
        if isinstance(other, Product):
            total_quantity = self.quantity + other.quantity
            total_price = (self.__price * self.quantity) + (other.__price * other.quantity)
            average_price = total_price / total_quantity
            new_product = Product(self.name, self.description, int(average_price), total_quantity)
            return new_product


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
    for product in category['products']:
        products.append(Product.new_product(product))
    category['products'] = products
    categories.append(Category(**category))

product_item = Product('Test', 'Test', 1000, 10)
print('product_item', product_item)

print(str(categories[0]) == 'Смартфоны, количество продуктов: 27 шт.')

print(str(product_item) == 'Test, 1000 руб. Остаток: 10 шт.')

product_item_2 = Product('Test2', 'Test2', 500, 20)

print(product_item + product_item_2 == 20000)