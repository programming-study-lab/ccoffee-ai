import streamlit as st
# from src.views.CaptionPageView import CaptionPageView
from src.services.AdminService import AdminService
from src.helpers.Router import Router


class LoginView:
    def __init__(self):
        self.adminService = AdminService()
        pass


    def run(self):
        # submit_butt = False
        with st.form("login form", clear_on_submit=True):
            st.title("เข้าสู่ระบบ")
            username = st.text_input("username")
            password = st.text_input("password", type="password", )
            submit_butt = st.form_submit_button("onLogin")

            if submit_butt:
                    
                result = self.adminService.onLogin(adminData={
                        "username": username,
                        "password": password
                })

                if result:
                    st.write(f'result: Ok')
                    st.session_state['login_status'] = True
                    st.switch_page("pages/1_Ccoffee Chat.py")
             
                    router = Router()
                    router.run()
                    
                    st.rerun()
             
                else:
                    st.error("เกิดข้อผิดพลาด")
