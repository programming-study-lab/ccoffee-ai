from src.services.MenuService import MenuService
from src.models.MenuModel import MenuModel

class SalesPageController:
    def __init__(self):
        self.menuService = MenuService()

    def getAllDataMenu(self):
        return self.menuService.read()

    def getMenu(self):
        dataService = self.menuService.read()
        menu = []

        for data in dataService:
            if data['quantity_status'] == "sale":
                menu.append(data['menu'])

        return menu
    
    def getPrice(self, menu):
        dataService = self.menuService.read()
        price = 0.0
        for data in dataService:
            if menu == data['menu']:
                price = float(data['price'])
                return price

        return 0.0

            
        

