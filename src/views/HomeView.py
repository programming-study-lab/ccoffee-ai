# app.py
import os

import streamlit as st
from dotenv import load_dotenv
from google import genai

from src.controllers.HomeController import HomeController

from rag_engine import RAGEngine
from src.controllers.ChatBotController import ChatBotController

class HomeView:
    def __init__(self):
        self.homeController = HomeController()
        

    def run(self):
        st.title("Cat ผู้ช่วย AI ของร้าน เสบียงเรียน (Study Fuel)")
        st.caption("ถามเรื่องเมนู เวลาเปิด หรือข้อมูลร้านได้เลย")

        st.set_page_config(layout="wide")

        st.sidebar.title("เมนู")
        
        allDataMenu = self.homeController.getAllDataMenu()

        for data in allDataMenu:
            st.sidebar.success(f"{data['id_menu']}: {data['menu']} ราคา {data['price']}")

        chatBotController = ChatBotController()
        chatBotController.setMenu(menu = allDataMenu)
        chatBotController.run()