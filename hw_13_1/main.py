"""
 Создайте классы Product и Category.
#
# Создайте классы Product и Category.
#
# Для класса Product:
#
# название (name),
# описание (description),
# цена (price),
# количество в наличии (quantity).

# Для класса Category определите следующие свойства:
#
# название (name),
# описание (description),
# список товаров категории (products).
# Для этих двух классов, добавьте инициализацию так, чтобы каждый параметр был передан
при создании объекта и сохранен.
#
# Также для класса Category добавьте два атрибута класса.
# Доступ к этим атрибутам должен быть у каждого объекта класса и в них должна
# храниться общая информация для всех объектов. Эти атрибуты хранят в себе количество
# категорий и количество товаров. Атрибуты класса должны заполняться автоматически при
# инициализации нового объекта.

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
        self.price = price
        self.quantity = quantity

        Product.category_count += 1
        Product.product_count += 1


class Category:
    """
    Класс для категорий товара
    """
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

        Category.category_count += 1
        Category.product_count += len(products)


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
        for product in category['products']:
            products.append(Product(**product))
        category['products'] = products

        categories.append(Category(**category))

    for category in categories:
        print(category.category_count)
        print(category.product_count)


check_homework()
