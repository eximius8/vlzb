from oscar.apps.shipping.models import *  # noqa isort:skip

from oscar.apps.shipping import repository
from . import methods


class Repository(repository.Repository):

    methods = (methods.Ultrafast(), methods.Standard(), methods.Express())

    def get_available_shipping_methods(self, basket, user=None, shipping_addr=None, request=None, **kwargs):

        methods = (methods.Ultrafast(), methods.Standard(), methods.Express())
        return methods
