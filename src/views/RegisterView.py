import streamlit as st
import bcrypt
from src.services.AdminService import AdminService

class RegisterView:
    def __init__(self):
        self.adminService = AdminService()
        pass


    def run(self):
        st.title("Register")

        username = st.text_input("username")
        password = st.text_input("password", type="password")
        re_password = st.text_input("re-password", type="password")
        butt_register = st.button("onRegister")

        if butt_register: 

            if password == re_password: 
                self.adminService.onRegister(adminData={
                    "username": username,
                    "password": password
                }) 
                pass

            else:
                st.warning("รหัสผ่านไม่ตรงกัน")


