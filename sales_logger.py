import datetime as dt
from datetime import timezone, timedelta
import os
from dotenv import load_dotenv
from sheets_client import get_sheet
import sys

load_dotenv()

if len(sys.argv) == 1:
    print("การใช้งาน: python sales_logger.py เมนู:จำนวน:ราคา")
    sys.exit(1)

try:
    menu, qty_str, price_str = sys.argv[1].split(':')
    quantity = int(qty_str)
    price = float(price_str)
    total = quantity * price
except ValueError as e:
    print(f"ป้อนข้อมูลไม่ถูกต้อง: {e}. รูปแบบ: เมนู:จำนวน:ราคา โดยจำนวนเป็นจำนวนเต็ม ราคาเป็นทศนิยม")
    sys.exit(1)

tz = timezone(timedelta(hours = 7))
now = dt.datetime.now(tz=tz)
# date_time_now = now.strftime("%Y-%m-%d %H:%M:%S")
date_time_now = now.strftime("%d/%m/%Y")

sheet = get_sheet()
sheet.append_row([date_time_now, menu, quantity, price, total])
print(f"บันทึกการขาย: {menu} x{quantity} ราคา {price} ฿ รวมเป็น {total} ฿")
print(f"success. : {date_time_now}")
