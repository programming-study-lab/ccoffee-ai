import streamlit as st
from src.controllers.CaptionController import CaptionController

class CaptionPageView:
    def __init__(self):
        self.captionController = CaptionController()

    def run(self):
        st.title("แคปชั่น") 
        menu = st.text_input("Menu")
        price = st.text_input("Price")
        butt_gen = st.button("สร้าง Caption")

        # butt_gen = st.form_submit_button("สร้าง Caption")
        
        captions = {
            'cute': '',
            'minimal': '',
            'gen_z': ''
        }

        if butt_gen:
            captions = self.captionController.generateCaptions(
               menu, price
            )

        # print(f"Cute: {captions['cute']}")
        # print(f"Minimal: {captions['minimal']}")
        # print(f"Gen_z: {captions['gen_z']}")
        
        st.write(f"Cute: {captions['cute']}")
        st.write(f"Minimal: {captions['minimal']}")
        st.write(f"Gen_z: {captions['gen_z']}")


        


