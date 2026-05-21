import streamlit as st
import os
from dotenv import load_dotenv

class Router:
    def __init__(self):
        # st.navigation()
        # if "login_status" not in st.session_state:
        if 'login_status' not in st.session_state:
            st.session_state['login_status'] = False  
            if st.session_state['login_status'] == False:
                if "userAccount" not in st.session_state:
                    st.session_state['userAccount'] = {
                        "user_status":""
                    }
        # if 'userAccount' not in st.session_state:
        #     st.session_state['userAccount'] = {
        #         'user_status':""
        #     }
        # pass

    def run(self):
        load_dotenv()
   
        # st.session_state['userAccount']
        # if st.session_state['userAccount']['user_status'] == "admin":
        
        # pages = {
        #         "Ccoffee ": [
        #                 st.Page("pages/2_Buy.py", title="Create your account"),
        #                 st.Page("pages/3_Caption.py", title="Manage your account"),
        # ],
        #         "Resources": [
        #                 # st.Page("learn.py", title="Learn about us"),
        #                 # st.Page("trial.py", title="Try it out"),
        #         ],
        # }
        print(f" ====== {st.session_state['userAccount']} =========")
        if st.session_state['userAccount']['user_status'] == os.getenv("ADMIN_KEY"):
            pages = {
                # "":"",
                "":[
                    st.Page("pages/1_Ccoffee Chat.py", title="Ccoffee Chat"), 
                    st.Page("pages/2_Buy.py", title="สั่งซื้อ")],
                
                "สำหรับพนักงาน": [
                        st.Page("pages/4_Login.py", title="เข้าสู่ระบบ"),
                        st.Page("pages/98_Register.py", title="เพิ่มพนักงาน"),
                        st.Page("pages/99_Logout.py", title="ออกจากระบบ")
                    ]
                
            }
        else:
            pages = {
                # "":"",
                "":[
                    st.Page("pages/1_Ccoffee Chat.py", title="Ccoffee Chat"), 
                    st.Page("pages/2_Buy.py", title="สั่งซื้อ")],
                
                "สำหรับพนักงาน": [
                    st.Page("pages/4_Login.py", title="เข้าสู่ระบบ")
                    ]
                
            }



        pg = st.navigation(pages)
        pg.run()