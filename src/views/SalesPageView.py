import streamlit as st
from src.models.SalesModel import SalesModel
from src.services.SalesService import SalesService
# from src.services.MenuService import MenuService
from src.controllers.SalesPageController import SalesPageController

class SalesPageView:
    def __init__(self):
        self.salesModel = SalesModel()
        self.salesService = SalesService()
        # self.menuService = MenuService()
        self.salesPageController = SalesPageController()
        # self.salesPageController.getMenu()

    def run(self):
        st.set_page_config(
            page_title="test",
            # page_icon="a"
        )

        st.title("สั่งซื้อ")
        st.sidebar.title("สั่งซื้อ")
        # st.sidebar.success(f"{self.salesPageController.getMenu()}")
        for data in self.salesPageController.getAllDataMenu():
            # st.sidebar.success(f"{data}")
            if data['quantity_status'] == "sale_out":
                st.sidebar.success(f"{data['menu']} ราคา {data['price']}")


        if "name" not in st.session_state:
            st.session_state["name"] = ""
        if "phone" not in st.session_state:
            st.session_state["phone"] = ""
        if "address" not in st.session_state:
            st.session_state["address"] = ""
        if "menu" not in st.session_state:
            st.session_state["menu"] = ""
        if "price" not in st.session_state:
            st.session_state['price'] = ""
        if "quantity" not in st.session_state:
            st.session_state['quantity'] = ""
        if "detail" not in st.session_state:
            st.session_state['detail'] = ""
        
        with st.form("สั่งซื้อสินค้า", clear_on_submit=True):
            name = st.text_input("ชื่อ", st.session_state["name"])
            phone = st.text_input("เบอร์โทร", st.session_state["phone"])
            address = st.text_input("ที่อยู่", st.session_state["address"])
            menu = st.selectbox("เมนู", self.salesPageController.getMenu())
            quantity = st.number_input("จำนวน", format="%d", min_value=1, max_value=21, step=1)
            # quantity = st.selectbox("จำนวน", ,)
            detail = st.text_input("รายละเอียด (ไม่ใส่ก็ได้)", st.session_state["detail"])
            # buy_butt = st.button("Buy")
            buy_butt = st.form_submit_button("Buy")

        # print(f"++++++++++++++++++ {self.salesPageController.getPrice(menu)}")
        # price = 40
        # quantity = 2

            if buy_butt:
                # print(f"{SalesModel(
                #     name=name,
                #     phone=phone,
                #     address=address,
                #     menu=menu,
                #     quantity=quantity,
                #     detail=detail
                # )}")
                # print(f"view: {quantity}")
                price = self.salesPageController.getPrice(menu)
                
                self.salesService.onBuy({
                    "name":name,
                    "phone":phone,
                    "address":address,
                    "menu":menu,
                    "price":price,
                    "quantity":quantity,
                    "detail":detail
                })


                st.session_state["name"] = ""
                st.session_state["phone"] = ""
                st.session_state["address"] = ""
                st.session_state["menu"] = ""
                st.session_state['price'] = ""
                st.session_state['quantity'] = ""
                st.session_state['detail'] = ""
                name = ''
                phone = ''
                address = ''
                menu = ''
                price = None
                quantity = ''
                detail = ''

                # st.navigator('./1_Ccoffee Chat.py')

                # self.show_popup()

    @st.dialog("Popup Window")
    def show_popup():
        st.write("This is a popup window!")
        # if st.button("Show Popup"):
        #     pass
            # st.warring("TTTTT")
            # self.salesService.onBuy(SalesModel(
            #     name=name,
            #     phone=phone,
            #     address=address,
            #     menu=menu,
            #     price=price,
            #     quantity=quantity,
            #     detail=detail
            # ))

            # pass