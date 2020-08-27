from oscar.apps.order.utils import OrderNumberGenerator as CoreOrderNumberGenerator


class OrderNumberGenerator(CoreOrderNumberGenerator):

    def order_number(self, basket=None):
        num = super().order_number(basket)
        return "vlz-%s" % num