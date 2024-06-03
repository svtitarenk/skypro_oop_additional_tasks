
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


class Product:
    """
    Класс для описания товара в магазине
    """
    name: str
    description: str
    __price: float
    quantity: int
    amount = 0

    @classmethod
    def new_product(cls, product):
        return cls(product['name'], product['description'], product['price'], product['quantity'])

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, product_price):
        if product_price <= 0:
            print('Цена не должна быть нулевая или отрицательная')
        else:
            self.__price = product_price

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        Product.amount += 1

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.\n'

    def __add__(self, other):
        if type(self) == type(other):
            return (self.__price * self.quantity) + (other.__price * other.quantity)
        else:
            raise TypeError


class Category:
    """
    Класс для категорий товара
    """
    name: str
    description: str
    __products: list
    amount_of_product = 0
    amount_of_category = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.amount_of_product = Product.amount
        Category.amount_of_category += 1

    def __str__(self):
        amount = 0
        for product in self.__products:
            amount += product.quantity
        return f'{self.name}, количество продуктов: {amount} шт.'

    @property
    def products(self):
        products = ''
        for product in self.__products:
            products += str(product)
        return products


    @products.setter
    def products(self, value):
        if not isinstance(value, Product):
            raise TypeError('Можно добавить только объекты класса Product или его наследников (Smartphone/LawnGrass)')
        self.__products.append(value)


class Smartphone(Product):

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self. memory = memory
        self.color = color


class LawnGrass(Product):

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


categories = []
for category in data:
    products = []
    for product in category['products']:
        products.append(Product(**product))
    category['products'] = products
    categories.append(Category(**category))

product_item = Product('Test', 'Test', 1000, 10)
product_item_2 = Smartphone('Test2', 'Test2', 2000, 10, 1.5,  'Xiaomi', 10000, 'red')
product_item_3 = LawnGrass('Test3', 'Test3', 3000, 10, 'Canada', '1 year', 'light green')

try:
    categories[0].products = 1
except TypeError:
    print('Можно добавить только объекты класса Product или его наследников (Smartphone/LawnGrass)')

categories[0].products = product_item
print(product_item.name in categories[0].products)



