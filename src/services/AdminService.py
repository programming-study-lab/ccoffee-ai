import datetime as dt
from datetime import timezone, timedelta
import os
from dotenv import load_dotenv
# from sheets_client import get_sheet
from src.databases.AdminGoogleSheetDatabase import AdminGoogleSheetDatabase
from src.models.SalesModel import SalesModel
import sys
import bcrypt
# pip install cryptography
from cryptography.fernet import Fernet
import streamlit as st

class AdminService:

    def __init__(self):
        self.adminGoogleSheetDatabase = AdminGoogleSheetDatabase
        # self.salesModel = SalesModel()

    def read(self):
        sheet = self.adminGoogleSheetDatabase.getSheet()
        # print(f"{sheet.get_all_records()}")
        return sheet.get_all_records()

    def onLogin(self, adminData = {
        "username": None,
        "password": None
    }):
        sheet = self.adminGoogleSheetDatabase.getSheet()
        admin = sheet.get_all_records()
        for verify in admin:
            if adminData['username'] == verify['username']:
        
                userPassword = adminData['password']
                userBytes = userPassword
                hash = verify['password']
                # print(f"++++++++++++ {userBytes} +++++++++++")
                # print(f"++++++++++++ {hash} +++++++++++")

                # virify['password'] = virify['password'].strip("b '")

                result = bcrypt.checkpw(adminData['password'].encode('utf-8'), verify['password'].encode('utf-8'))

                if (result):
             
                    # if "userAccount" not in st.session_state:
                    st.session_state['userAccount'] = {
                        "username": verify['username'],
                        "user_status": verify['user_status']
                    }


                    return True
                else:
                    return False

        return False




    def onRegister(self, adminData = {
        "uesrname": None,
        "password": None
    }):
        load_dotenv()
        hash = 'test'
        try:
            username = adminData['username']
            password = adminData['password']
            # print(f"{adminData}")
            salt = bcrypt.gensalt(rounds=10)
            passwordBytes = password.encode('utf-8')
            hash = bcrypt.hashpw(passwordBytes, salt)

            
        except ValueError as e:
            print(f"ป้อนข้อมูลไม่ถูกต้อง: {e}.")
            sys.exit(1)

        tz = timezone(timedelta(hours = 7))
        now = dt.datetime.now(tz=tz)
        # date_time_now = now.strftime("%Y-%m-%d %H:%M:%S")
        date_time_now = now.strftime("%d/%m/%Y")
        sheet = self.adminGoogleSheetDatabase.getSheet()
        # sheet.append_row([username, f'{hash}'])
        sheet.append_row([username, hash.decode()])
        print(f"Register success. : {date_time_now}")
