class Customer:
    '''
    Класс `Customer` хранит информацию о клиентах и их заказах.
    Customer - класс, представляющий клиента, с атрибутами name (имя клиента) и orders (список заказов клиента).

    '''



    def __init__(self, name):
        self.name = name
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def __str__(self):
        return f'Покупатель(имя={self.name}, количество заказов={len(self.orders)})'

    def __repr__(self):
        return f'Покупатель({self.name!r})'