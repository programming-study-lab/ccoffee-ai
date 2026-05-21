
class MenuModel:
    id_manu = ''
    menu = ''
    price = ''
    quantity_status = ''
    detail = ''

    def __init__(self, 
                 id_menu= None,
                 menu=None,
                 price=None,
                 quantity_status=None,
                 detail=None):
        self.id_menu = id_menu
        self.menu = menu
        self.price = price
        self.quantity_status = quantity_status
        self.detail = detail
        pass



