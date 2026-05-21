try:
    from src.views.LoginView import LoginView
    
    loginView = LoginView()
    loginView.run()
except Exception as e:
    import streamlit as st
    st.title("ข้ออภัย เกิดข้อผิดพลาดบางประการ")


# import streamlit as st
# # from src.views.CaptionPageView import CaptionPageView
# from src.services.AdminService import AdminService


# class Login:
#     def __init__(self):
#         self.adminService = AdminService()
#         pass


#     def loginPage(self):
#         # loginPage = st.button("login")

#         # self.registerPage()      
     
#         # butt_login = False
#         # if not butt_login:
#         submit_butt = False
#         with st.form("login form", clear_on_submit=True):
#             st.title("Login Caption")
#             username = st.text_input("username")
#             password = st.text_input("password", type="password", )
#             # butt_login = st.button("onLogin")
#             submit_butt = st.form_submit_button("onLogin")
#             # st.rerun()


#             if submit_butt:
                    
#                 result = self.adminService.onLogin(adminData={
#                         "username": username,
#                         "password": password
#                 })

#                 if result:
#                     st.write(f'result: Ok')
#                     # if "login_status" in st.sesstion_state:
#                     st.session_state['login_status'] = True
#                     # st.navigation()
#                     print(f"++++++++ {st.session_state['login_status']} +++++++++++")
#                     st.switch_page("pages/3_Caption.py")
#                     st.rerun()
   
             
#                 else:
#                     st.error("เกิดข้อผิดพลาด")

            

#     # def run(self):

#     #     captionPageView = CaptionPageView()
#     #     captionPageView.run()


# # captionLogin = CaptionLogin()
# if __name__ == "__main__":
#     captionLogin = Login()

#     buy_page = st.Page(
#         page='pages/2_Buy.py',
#         title="Buy",
#         icon = None,
#         default = False
#     )
#     captionLogin.loginPage()
