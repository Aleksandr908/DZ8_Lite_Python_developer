class Product:
    """
    Класс Product
    Класс Product содержит информацию о продукте и реализует методы для сравнения.
    Этот класс представляет товар в интернет-магазине.
    Product - класс, представляющий товар, с атрибутами name (название товара) и price (цена товара).
    Метод __init__:
        Конструктор инициализирует объект Product с двумя атрибутами: name (название товара) и price (цена товара).
        Пример: product1 = Product("Laptop", 1000) создаст товар с названием "Laptop" и ценой 1000.

    Метод __str__:
        Возвращает строковое представление объекта, чтобы его можно было удобно вывести с помощью print.
        Пример: print(product1) выведет Product(name=Laptop, price=1000).
    """
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Продукт (Название={self.name}, Цена={self.price})"

    def __repr__(self):
        return f'Продукт ({self.name!r}, {self.price})'

    def __eq__(self, other):
        return self.price == other.price

    def __lt__(self, other):
        return self.price < other.price