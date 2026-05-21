

class SalesModel:
    test = ''
    phone = ''
    name = ''
    menu = ''
    price = ''
    quantity = ''
    detail = ''
    
    def __init__(self, 
                 phone = None, 
                 name = None,
                 address = None,
                 menu = None,
                 price = None,
                 quantity = None,
                 detail = None
                 ):
        print(f"{price}")
        self.phone = phone
        self.name = name
        self.address = address
        self.menu = menu
        self.price = price
        self.quantity = quantity
        self.detail = detail

    def fromMap(self,map = {
            "phone": None,
            "name": None,
            "address": None,
            "menu": None,
            "price": None,
            "quantity": None,
            "detail": None
        }
    ):
        return SalesModel(
            phone = map['phone'], 
            name = map['name'],
            address = map['address'],
            menu = map['menu'],
            price = map['price'],
            quantity = map['quantity'],
            detail = map['detail']
        )

    def toMap(self):
        return {
            "phone": self.phone,
            "name": self.name,
            "address": self.address,
            "menu": self.menu,
            "price": self.price,
            "quantity": self.quantity,
            "detail": self.detail
        }
    
    def getPrice(self):
        return self.price
    
    def getQuantity(self):
        return self.quantity