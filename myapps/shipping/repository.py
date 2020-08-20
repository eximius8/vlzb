from oscar.apps.shipping import repository
from . import methods


class Repository(repository.Repository):

    def get_available_shipping_methods(self, basket, user=None, shipping_addr=None, request=None, **kwargs):

        all_methods = (methods.Reserve(),)
        if shipping_addr and shipping_addr.state == 'VLZ':            
            
            all_methods = (methods.Reserve(), methods.Vlzship())
        elif shipping_addr and (shipping_addr.state == 'VLG' or shipping_addr.state == 'KRA'):            
            
            all_methods = (methods.Reserve(), methods.VlgKraship())

        elif shipping_addr and shipping_addr.state == 'SRA':  
            
            all_methods = (methods.Reserve(), methods.Sraship())

        return all_methods#( methods.Reserve(), methods.Ultrafast(), methods.Express(), methods.Standard())
