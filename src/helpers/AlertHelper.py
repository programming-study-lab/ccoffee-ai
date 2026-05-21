import streamlit as st

class AlertHelper:

    @st.dialog("Popup Window")
    def show_popup():
        st.write("This is a popup window!")
        if st.button("Show Popup"):
            st.warring("TTTTT")