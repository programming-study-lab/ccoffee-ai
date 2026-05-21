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
        # st.title("Ccoffee")
        st.title("🥛 Cat ผู้ช่วย AI ของ Ccoffee")
        st.caption("ถามเรื่องเมนู เวลาเปิด หรือข้อมูลร้านได้เลย")

        st.set_page_config(layout="wide")

        st.sidebar.title("about")

                # st.header("Intructions")

        load_dotenv()
        client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
        MODEL = "gemini-2.5-flash"

        for data in self.homeController.getAllDataMenu():
            st.sidebar.success(f"{data['menu']} ราคา {data['price']}")
            # butt = st.button(f"{data['menu']} ราคา {data['price']}")

        @st.cache_resource
        def load_rag():
            return RAGEngine("knowledge/ccoffee_kb.txt")

        rag = load_rag()

        if "messages" not in st.session_state:
            st.session_state.messages = []

        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.write(msg["content"])

        if prompt := st.chat_input("ถามอะไรเกี่ยวกับร้านได้เลย..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.write(prompt)

            # RAG: Search
            context_chunks = rag.search(prompt, top_k=3)
            context = "\n---\n".join(context_chunks)

            # Generate
            full_prompt = f"""คุณคือ Cat ผู้ช่วย AI ของร้าน Ccoffee ตอบเฉพาะจากข้อมูลด้านล่าง
                                ถ้าไม่พบข้อมูล ให้บอกว่าไม่ทราบ อย่าแต่งข้อมูลเอง

                                ข้อมูลร้าน:
                                {context}

                                คำถาม: {prompt}
                            """
                            
            response = client.models.generate_content(model=MODEL, contents=full_prompt)
            answer = response.text

            st.session_state.messages.append({"role": "assistant", "content": answer})
            with st.chat_message("assistant"):
                st.write(answer)