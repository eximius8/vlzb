from oscar.apps.shipping import methods
from oscar.core import prices
from decimal import Decimal as D

class Standard(methods.Base):
    code = 'standard'
    name = 'Standard shipping (free)'

    def calculate(self, basket):
        return prices.Price(
            currency=basket.currency,
            excl_tax=D('0.00'), incl_tax=D('0.00'))

class Ultrafast(methods.FixedPrice):
    code = 'ufast'
    name = 'Ultrafast shipping'

    def calculate(self, basket):
        return prices.Price(
            currency=basket.currency,
            excl_tax=D('1430.00'), incl_tax=D('4321.00'))

class Reserve(methods.NoShippingRequired):
    code = 'RESERVE'
    name = 'Reserve'
    description = 'Items will be reserved at the warehouse for 7 days'


class Express(methods.FixedPrice):
    code = 'express'
    name = 'Express shipping'

    def calculate(self, basket):
        return prices.Price(
            currency=basket.currency,
            excl_tax=D('10.00'), incl_tax=D('1.00'))
