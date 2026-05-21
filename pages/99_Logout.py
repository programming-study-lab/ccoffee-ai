
try:
    import streamlit as st
    from src.views.LogoutView import LogoutView

    if "login_status" not in st.session_state:
        st.session_state['login_status'] = False
    if st.session_state['login_status']:
        logoutView = LogoutView()
        logoutView.run()
    else:
        st.write("กรุณาเข้าสู่ระบบ")


    # class Logout:
    #     def run(self):
    #         st.session_state['login_status'] = False

    #         for key in list(st.session_state):
    #             del st.session_state[key]

    # st.title("คุณต้องการออกจากระบบหรือไม่?")
    # logout = st.button("ออกจากระบบ")
    # if logout:
    #     logout = Logout()
    #     logout.run()

except Exception as e:
    st.title("เกิดข้อผิดพลาด")