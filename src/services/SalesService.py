import datetime as dt
from datetime import timezone, timedelta
import os
from dotenv import load_dotenv
from src.databases.SalesGoogleSheetDatabase import SalesGoogleSheetDatabase
from src.models.SalesModel import SalesModel
import sys

class SalesService:

    def __init__(self):
        self.salesGoogleSheetDatabase = SalesGoogleSheetDatabase

    def read(self):
        sheet = self.salesGoogleSheetDatabase.getSheet()
        return sheet.get_all_records()

    def onBuy(self, data):
        self.read()
        load_dotenv()
        salesModel = SalesModel(
            name=data['name'],
            phone=data['phone'], 
            address = data['address'],
            detail=data['detail'],
            menu=data['menu'],
            price=data['price'],
            quantity=data['quantity'],
            )
        try:
            quantity = int(salesModel.quantity)
            price = float(salesModel.price)
            total = quantity * price
        except ValueError as e:
            print(f"ป้อนข้อมูลไม่ถูกต้อง: {e}. รูปแบบ: เมนู:จำนวน:ราคา โดยจำนวนเป็นจำนวนเต็ม ราคาเป็นทศนิยม")
            sys.exit(1)

        tz = timezone(timedelta(hours = 7))
        now = dt.datetime.now(tz=tz)
        date_time_now = now.strftime("%d/%m/%Y").strip("\'")

        sheet = self.salesGoogleSheetDatabase.getSheet()
        sheet.append_row([date_time_now, salesModel.name, salesModel.phone, salesModel.address, salesModel.detail, salesModel.menu, quantity, price, total])
        print(f"บันทึกการขาย: {data['menu']} x{quantity} ราคา {price} ฿ รวมเป็น {total} ฿")
        print(f"success. : {date_time_now}")
