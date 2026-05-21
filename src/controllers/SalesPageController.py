from src.services.MenuService import MenuService
from src.models.MenuModel import MenuModel

class SalesPageController:
    def __init__(self):
        self.menuService = MenuService()

    def getAllDataMenu(self):
        return self.menuService.read()

    def getMenu(self):
        # menuMode = MenuModel
        dataService = self.menuService.read()
        menu = []
        # print(f"{menuService.read()}")

        # print(f"++++++++++++++++++++ {len(dataService)} ++++++++++++++++++++++++++")
        for data in dataService:
            menu.append(data['menu'])
            # print(f"++++++++++++++++++++ {data} ++++++++++++++++++++++++++")

        # return menuService.read() 
        return menu
    
    def getPrice(self, menu):
        dataService = self.menuService.read()
        price = 0.0
        for data in dataService:
            if menu == data['menu']:
                price = float(data['price'])
                return price

        return 0.0

            
        

