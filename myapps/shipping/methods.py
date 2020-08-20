from oscar.apps.shipping import methods
from oscar.core import prices
from decimal import Decimal as D

class Reserve(methods.Base):
    code = 'standard'
    name = 'Самовывоз из магазина в Волжском по адресу: 404130 Коммунистическая 36 (товар будет зарезервирован на 5 дней)'

    def calculate(self, basket):
        return prices.Price(
            currency=basket.currency,
            excl_tax=D('0.00'), incl_tax=D('0.00'))

class Vlzship(methods.FixedPrice):
    code = 'ufast-vlz'
    name = 'Доставка курьером по Волжскому'

    def calculate(self, basket):
        return prices.Price(
            currency=basket.currency,
            excl_tax=D('50.00'), incl_tax=D('50.00'))

class VlgKraship(methods.FixedPrice):
    code = 'ufast-vlg'
    name = 'Доставка курьером по Волгограду и Краснослободску'

    def calculate(self, basket):
        return prices.Price(
            currency=basket.currency,
            excl_tax=D('250.00'), incl_tax=D('250.00'))

class Sraship(methods.FixedPrice):
    code = 'ufast-sra'
    name = 'Доставка курьером в Среднюю Ахтубу'

    def calculate(self, basket):
        return prices.Price(
            currency=basket.currency,
            excl_tax=D('150.00'), incl_tax=D('150.00'))


