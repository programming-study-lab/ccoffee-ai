import streamlit as st

class LogoutController:

    def onLogout():
        st.session_state['login_status'] = False

        for key in list(st.session_state):
            del st.session_state[key]