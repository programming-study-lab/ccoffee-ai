try:
        from src.views.HomeView import HomeView

        homeView = HomeView()
        homeView.run()
        
except Exception as e:
        import streamlit as st
        st.write("ข้ออภัย เกิดข้อผิดพลาดบางประการ กรุณาลองใหม่อีกครั้ง")