import streamlit as st
from src.controllers.LogoutController import LogoutController

class LogoutView:

    def run(self):
        st.title("คุณต้องการออกจากระบบหรือไม่?")
        logout = st.button("ออกจากระบบ")
        if logout:
            logoutController = LogoutController()
            logoutController.onLogout()
        

        

    


    