try:
    from src.helpers.Router import Router
    router = Router()
    router.run()

except Exception as e:
    import streamlit as st
    st.title(f"เกิดข้อผิดพลาดบางประการ \n {e}")
