import streamlit as st
from src.models.SalesModel import SalesModel
from src.services.SalesService import SalesService
# from src.services.MenuService import MenuService
from src.controllers.SalesPageController import SalesPageController
from src.helpers.AlertHelper import AlertHelper

class SalesPageView:
    def __init__(self):
        self.salesModel = SalesModel()
        self.salesService = SalesService()
        # self.menuService = MenuService()
        self.salesPageController = SalesPageController()
        if "input_status" not in st.session_state:
            st.session_state['input_status'] = {
                "nameIsNull": False, 
                "phoneIsNull": False,
                "addressIsNull": False,
                "menuIsNull": False 
            }
        if "clearOnSubmit" not in st.session_state: 
            st.session_state['clearOnSubmit'] = False

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
        # self.salesPageController.getMenu()

    def run(self):
        st.set_page_config(
            page_title="test",
            # page_icon="a"
        )

        st.title("สั่งซื้อ")
        st.sidebar.title("เมนู")
        # st.sidebar.success(f"{self.salesPageController.getMenu()}")
        for data in self.salesPageController.getAllDataMenu():
            # st.sidebar.success(f"{data}")
            if data['quantity_status'] != "sold_out":
                st.sidebar.success(f"{data['menu']} ราคา {data['price']}")

        # st.warning(f"{st.session_state['clearOnSubmit']} || {st.session_state}") 
        with st.form("สั่งซื้อสินค้า", clear_on_submit=True):

            name = st.text_input("ชื่อ (จำเป็น)", st.session_state["name"])
            st.session_state['name'] = name
            if st.session_state['input_status']['nameIsNull'] == True:
                st.warning("กรุณาเพิ่มข้อมูลชื่อ")

            phone = st.text_input("เบอร์โทร (จำเป็น)", st.session_state["phone"])
            st.session_state['phone'] = phone
            if st.session_state['input_status']['phoneIsNull'] == True:
                st.warning("กรุณาเพิ่มข้อมูลเบอร์โทร")

            address = st.text_input("ที่อยู่ (จำเป็น)", st.session_state["address"])
            st.session_state['address'] = address
            if st.session_state['input_status']['addressIsNull'] == True:
                st.warning("กรุณาเพิ่มข้อมูลที่อยู่")

            menu = st.selectbox("เมนู (จำเป็น)", self.salesPageController.getMenu())
            st.session_state['menu'] = menu
            if st.session_state['input_status']['menuIsNull'] == True:
                st.warning("กรุณาเพิ่มข้อมูลเมนู")

            quantity = st.number_input("จำนวน (น้อยสุด = 1, มากสุด = 21)", format="%d", min_value=1, max_value=21, step=1)
            # quantity = st.selectbox("จำนวน", ,)
            detail = st.text_input("รายละเอียด (ไม่ใส่ก็ได้)", st.session_state["detail"])
            st.session_state['detail'] = detail
            # buy_butt = st.button("Buy")
            buy_butt = st.form_submit_button("Buy")

            if buy_butt:
                try:
                    if name == '':
                        st.session_state['input_status']['nameIsNull'] = True
                        st.rerun()
                    elif phone == '':
                        st.session_state['input_status']['phoneIsNull'] = True
                        st.rerun()
                    elif address == '':
                        st.session_state['input_status']['addressIsNull'] = True
                        st.rerun()
                    elif menu == '':
                        st.session_state['input_status']['menuIsNull'] = True
                        st.rerun()
                    else:
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
                        st.session_state['input_status']['nameIsNull'] = False
                        st.session_state['input_status']['phoneIsNull'] = False
                        st.session_state['input_status']['addressIsNull'] = False
                        st.session_state['input_status']['menuIsNull'] = False
                        st.session_state['clearOnSubmit'] = False

                        alertHelper = AlertHelper(
                        title="สั่งซื้อสำเร็จ", 
                        message="ขอบคุณสำหรับการสั่งซื้อ"
                        )
                        alertHelper.showPopUp()

                except Exception as e:
                    alertHelper = AlertHelper(
                        title="เกิดข้อผิดพลาด", 
                        message=f"ขออภัยในความไม่สะดวก"
                        )
                    alertHelper.showPopUp()
                    pass

                # st.navigator('./1_Ccoffee Chat.py')

                # self.show_popup()
