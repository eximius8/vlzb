from oscar.apps.shipping.models import *  # noqa isort:skip

from oscar.apps.shipping import repository
from . import methods


class Repository(repository.Repository):
    methods = (methods.Standard())#, methods.Express())