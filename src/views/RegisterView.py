import streamlit as st
import bcrypt
from src.services.AdminService import AdminService
from src.helpers.AlertHelper import AlertHelper

class RegisterView:
    def __init__(self):
        self.adminService = AdminService()
        pass


    def run(self):

            with st.form("register form", clear_on_submit=True):
                st.title("เพิ่มพนักงาน")
                username = st.text_input("username")
                password = st.text_input("password", type="password", )
                re_password = st.text_input("re-password", type="password")
                submit_butt = st.form_submit_button("เพิ่มพนักงาน")

                if submit_butt:
                    if password == re_password: 
                        self.adminService.onRegister(adminData={
                            "username": username,
                            "password": password
                        }) 
                        alertHelper = AlertHelper(
                            message="เพิ่มพนักงานสำเร็จ"
                        )
                        alertHelper.showPopUp()
                        pass

                    else:
                        st.warning("รหัสผ่านไม่ตรงกัน")
        
            


