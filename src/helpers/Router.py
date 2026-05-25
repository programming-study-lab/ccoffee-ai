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

        if st.session_state['userAccount']['user_status'] == os.getenv("ADMIN_KEY"):
            pages = {
                "":[
                    st.Page("pages/1_Ccoffee Chat.py", title="เสบียงเรียน Chat"), 
                    st.Page("pages/2_Buy.py", title="สั่งซื้อ")],
                
                "สำหรับพนักงาน": [
                        st.Page("pages/3_Caption.py", title="ขายอะไรบ้าง?"),
                        st.Page("pages/98_Register.py", title="เพิ่มพนักงาน"),
                        st.Page("pages/99_Logout.py", title="ออกจากระบบ")
                    ]
                
            }
        else:
            pages = {
                "":[
                    st.Page("pages/1_Ccoffee Chat.py", title="ขายอะไรบ้าง?"), 
                    st.Page("pages/2_Buy.py", title="สั่งซื้อ")],
                
                "สำหรับพนักงาน": [
                    st.Page("pages/4_Login.py", title="เข้าสู่ระบบ")
                    ]
                
            }



        pg = st.navigation(pages)
        pg.run()