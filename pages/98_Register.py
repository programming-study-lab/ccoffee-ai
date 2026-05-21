
try:
    import streamlit as st
    from src.views.RegisterView import RegisterView

    if "login_status" not in st.session_state:
        st.session_state['login_status'] = False
    if st.session_state['login_status']:
        registerView = RegisterView()
        registerView.run()
    else:
        st.write("กรุณาเข้าสู่ระบบ")

except Exception as e:
    # import streamlit as st
    st.title(f"ข้ออภัย เกิดข้อผิดพลาด")