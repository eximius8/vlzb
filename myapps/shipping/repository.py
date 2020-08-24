from oscar.apps.shipping import repository
from . import methods


class Repository(repository.Repository):

    def get_available_shipping_methods(self, basket, user=None, shipping_addr=None, request=None, **kwargs):

        all_methods = (methods.Reserve(),)
        if shipping_addr and shipping_addr.state == 'Волжский':            
            
            all_methods = (methods.Reserve(), methods.Vlzship(),)
        elif shipping_addr and (shipping_addr.state == 'Волгоград' or shipping_addr.state == 'Краснослободск'):            
            
            all_methods = (methods.Reserve(), methods.VlgKraship(), methods.PochtaRu())

        elif shipping_addr and shipping_addr.state == 'Средняя Ахтуба':  
            
            all_methods = (methods.Reserve(), methods.Sraship(),)

        return all_methods#( methods.Reserve(), methods.Ultrafast(), methods.Express(), methods.Standard())
