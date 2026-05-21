import streamlit as st
from src.helpers.Router import Router

class LogoutController:

    def onLogout(self):

        for key in list(st.session_state):
            del st.session_state[key]

        st.session_state['login_status'] = False
        st.session_state['userAccount'] = {
            "user_status":""
        }

        st.switch_page("pages/1_Ccoffee Chat.py")
        
        router = Router()
        router.run()