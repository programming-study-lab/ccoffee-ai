try:
        from src.views.HomeView import HomeView

        homeView = HomeView()
        homeView.run()
        
except Exception as e:
        import streamlit as st
        st.title("ข้ออภัย เกิดข้อผิดพลาดบางประการ")