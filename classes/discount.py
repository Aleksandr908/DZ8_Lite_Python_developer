class Discount:
    '''
    Discount - класс для применения скидок, с атрибутами description (описание скидки) и discount_percent (процент скидки).
    Класс `Discount` имеет статические методы для расчета цены со скидкой и применения различных типов скидок.

    '''


    def __init__(self, description, discount_percent):
        self.description = description
        self.discount_percent = discount_percent

    @staticmethod
    def apply_discount(price, discount_percent):
        return price * (1 - discount_percent / 100)

    @staticmethod
    def seasonal_discount(price):
        return Discount.apply_discount(price, 10)  # 10% сезонная скидка

    @staticmethod
    def promo_code_discount(price):
        return Discount.apply_discount(price, 15)  # 15% скидка по промокоду

    def __str__(self):
        return f'Скидка(описание={self.description}, процент скидки={self.discount_percent})'

    def __repr__(self):
        return f'Скидка({self.description!r}, {self.discount_percent})'