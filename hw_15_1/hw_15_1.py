class Product:
    """
    Класс для описания товара в магазине
    """
    name: str
    description: str
    price: int
    quantity: int

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
        if type(self) != type(other):
            raise TypeError("Нельзя складывать товары разных классов")
        else:
            return (self.__price * self.quantity) + (other.__price * other.quantity)


class Smartphone(Product):
    """ Для магазина необходимо выделить две категории товаров и создать под них классы: Смартфон (Smartphone)
    Помимо имеющихся свойств, необходимо добавить следующие:
        производительность (efficiency),
        модель (model),
        объем встроенной памяти (memory),
        цвет (color).
    """

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if type(other) is Smartphone:
            return (self.price * self.quantity) + (other.price * other.quantity)
        else:
            raise TypeError("Нельзя складывать товары разных классов")


class LawnGrass(Product):
    """  Для магазина необходимо выделить две категории товаров и создать под них классы: Трава газонная (LawnGrass)
    страна-производитель (country),
    срок прорастания (germination_period),
    цвет (color).
    """

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(other) is LawnGrass:
            return (self.price * self.quantity) + (other.price * other.quantity)
        else:
            raise TypeError("Нельзя складывать товары разных классов")


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

    # @product.setter
    # def product(self, product):
    #     self.__products.append(product)

    @products.setter
    def products(self, prod: Product):
        if isinstance(prod, Product):
            self.__products.append(prod.name)
        else:
            raise TypeError

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

if __name__ == "__main__":
    # product1 = Product('Product1', "Description1", 150, 1)
    # product2 = Product('Product2', "Description2", 150, 1)
    #
    # smartphone1 = Smartphone('name1', 'description1', 10, 1, 'efficiency1', 'model1', 'memory1', 'color1')
    # smartphone2 = Smartphone('name2', 'description2', 20, 1, 'efficiency2', 'model2', 'memory2', 'color2')
    #
    # lawngrass1 = LawnGrass('name1', 'description1', 22, 2, 'country1', 'germination_period1', 'color1')
    # lawngrass2 = LawnGrass('name2', 'description2', 11, 3, 'country2', 'germination_period2', 'color2')
    #
    # print(smartphone1.price, smartphone1.quantity)
    #
    # sm2 = smartphone1 + smartphone2
    # print('smartphones:', sm2)
    #
    # sm = product1 + product2
    # print('products', sm)
    #
    # sm_grass = lawngrass1 + lawngrass2
    # print('sm_grass:', sm_grass)
    #
    # sm_other = lawngrass1 + lawngrass2
    # print('sm_error:', sm_other)


    """тест 1"""

    # categories = []
    # for category in data:
    #     products = []
    #     for product in category['products']:
    #         products.append(Product.new_product(product))
    #     category['products'] = products
    #     categories.append(Category(**category))
    #
    # product_item = Product('Test', 'Test', 1000, 10)
    # product_item_2 = Smartphone('Test2', 'Test2', 2000, 10, 1.5,  'Xiaomi', 10000, 'red')
    # product_item_3 = LawnGrass('Test3', 'Test3', 3000, 10, 'Canada', '1 year', 'light green')
    #
    #
    # try:
    #     product_item + product_item_2
    # except TypeError:
    #     print('Ошибка сложения. Нельзя складывать не экземпляры одного класса')
    #
    # print( product_item + product_item == 20000)

    """ Тест 2 """

    # categories = []
    # for category in data:
    #     products = []
    #     for product in category['products']:
    #         products.append(Product.new_product(product))
    #     category['products'] = products
    #     categories.append(Category(**category))
    #
    # product_item = Product('Test', 'Test', 1000, 10)
    # product_item_2 = Smartphone('Test2', 'Test2', 2000, 10, 1.5, 'Xiaomi', 10000, 'red')
    # product_item_3 = LawnGrass('Test3', 'Test3', 3000, 10, 'Canada', '1 year', 'light green')
    #
    # try:
    #     categories[0].products = 1
    # except TypeError:
    #     print('Можно добавить только объекты класса Product или его наследников (Smartphone/LawnGrass)')
    #
    # categories[0].products = product_item
    # print(product_item.name in categories[0].products)

    """ Тест 3 """

    # categories = []
    # for category in data:
    #     products = []
    #     for product in category['products']:
    #         products.append(Product.new_product(product))
    #     category['products'] = products
    #     categories.append(Category(**category))
    #
    # product_item = Product('Test', 'Test', 1000, 10)
    # product_item_2 = Smartphone('Test2', 'Test2', 2000, 10, 1.5, 'Xiaomi', 10000, 'red')
    # product_item_3 = LawnGrass('Test3', 'Test3', 3000, 10, 'Canada', '1 year', 'light green')
    #
    # print(product_item_2.name)
    # print(product_item_2.quantity)
    # print(product_item_2.description)
    # print(product_item_2.price)
    # print(product_item_2.efficiency)
    # print(product_item_2.model)
    # print(product_item_2.model)
    # print(product_item_2.memory)
    # print(product_item_2.color)

    """ Тест 4 """

    # categories = []
    # for category in data:
    #     products = []
    #     for product in category['products']:
    #         products.append(Product.new_product(product))
    #     category['products'] = products
    #     categories.append(Category(**category))
    #
    # product_item = Product('Test', 'Test', 1000, 10)
    # product_item_2 = Smartphone('Test2', 'Test2', 2000, 10, 1.5, 'Xiaomi', 10000, 'red')
    # product_item_3 = LawnGrass('Test3', 'Test3', 3000, 10, 'Canada', '1 year', 'light green')
    #
    # print(product_item_3.country)
    # print(product_item_3.germination_period)
    # print(product_item_3.color)
    # print(product_item_3.name)
    # print(product_item_3.description)
    # print(product_item_3.price)
    # print(product_item_3.quantity)