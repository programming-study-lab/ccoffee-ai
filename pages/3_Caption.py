try:
    import streamlit as st
    from src.views.CaptionPageView import CaptionPageView
    from src.services.AdminService import AdminService


    class CaptionLogin:
        def __init__(self):
            self.adminService = AdminService()
            pass

        def run(self):

            captionPageView = CaptionPageView()
            captionPageView.run()


    captionLogin = CaptionLogin()
    if "login_status" not in st.session_state:
        st.session_state['login_status'] = False
    elif st.session_state['login_status'] == True:
        captionLogin.run()
    else:
        st.write("กรุณาเข้าสู่ระบบ")

except Exception as e:
    st.write("เกิดข้อผิดพลาดบางประการ ข้ออภัยในความไม่สะดวก")
