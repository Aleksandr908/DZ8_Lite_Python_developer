class Order:
    """
    Класс Order

    Этот класс представляет заказ в интернет-магазине.

    Атрибут класса _total_orders:
        Счетчик всех созданных заказов. Это атрибут класса, а не экземпляра, поэтому он общий для всех объектов Order.

    Метод __init__:
        Конструктор принимает список товаров (products) и инициализирует объект Order.
        Увеличивает счетчик _total_orders на 1 каждый раз при создании нового заказа.
        Пример: order1 = Order([product1]) создаст заказ, содержащий один товар.

    Метод calculate_discounted_price:
        Статический метод, который принимает цену и скидку в процентах и возвращает цену после применения скидки.
        Пример: Order.calculate_discounted_price(1000, 10) вернет 900.0.

    Метод total_orders:
        Метод класса, который возвращает общее количество созданных заказов.
        Пример: Order.total_orders() вернет общее количество заказов.

    Метод total_price:
        Вычисляет общую стоимость всех товаров в заказе, суммируя их цены.
        Пример: order1.total_price() вернет 1000, если в заказе один товар с ценой 1000.

    Метод __str__:
        Возвращает строковое представление объекта заказа, включающее общую стоимость заказа.
        Пример: print(order1) выведет Order(total_price=1000).
    """
    all_orders = []

    def __init__(self):
        self.products = []
        Order.all_orders.append(self)

    def add_product(self, product):
        self.products.append(product)

    @classmethod
    def total_orders_count(cls):
        return len(cls.all_orders)

    @classmethod
    def total_orders_sum(cls):
        return sum(sum(product.price for product in order.products) for order in cls.all_orders)

    def __str__(self):
        products_list = ', '.join(str(product) for product in self.products)
        return f'Заказ(Продукты=[{products_list}])'

    def __repr__(self):
        return f'Заказ({self.products!r})'