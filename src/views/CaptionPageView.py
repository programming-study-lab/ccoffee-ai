import streamlit as st
from src.controllers.CaptionController import CaptionController

class CaptionPageView:
    def __init__(self):
        self.captionController = CaptionController()

    def run(self):
        st.title("แคปชั่น") 
        menu = st.text_input("Menu")
        price = st.number_input("Price", format="%d", min_value=0, max_value=1000, step=1)
        butt_gen = st.button("สร้าง Caption")

        captions = {
            'cute': '',
            'minimal': '',
            'gen_z': ''
        }

        if butt_gen:
            captions = self.captionController.generateCaptions(
               menu, price
            )
        
        st.write(f"Cute: {captions['cute']}")
        st.write(f"Minimal: {captions['minimal']}")
        st.write(f"Gen_Z: {captions['gen_z']}")


        


