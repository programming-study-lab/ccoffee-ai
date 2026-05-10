import os
from dotenv import load_dotenv
from sheets_client import get_sheet
import requests
from datetime import datetime, timedelta

load_dotenv()

def send_telegram_msg(message):
    telegram_bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    telegram_chat_id = os.getenv('TELEGRAM_CHAT_ID')
    url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage"
    payload = {"chat_id": telegram_chat_id, "text": message, "parse_mode": "Markdown"}
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print(f"อุ๊ย! ส่งข้อความไม่สำเร็จ: {e}")
    
def main():
    sheet = get_sheet()
    data = sheet.get_all_records()
    yesterday = (datetime.now() - timedelta(days=1)).strftime('%d/%m/%Y')

    if not yesterday:
        send_telegram_msg(f"ฮัลโหลลล~ เมื่อวาน ({yesterday}) เงียบเหงาจังเลย ไม่มีออเดอร์เลยค่าาา 😅")
        return
    
    yesterday_sales = []
    for d in data:
        if d['date'] == yesterday:
            yesterday_sales.append(d)



    total_sales = 0
    menu_count = {}
    for sale in yesterday_sales:
        price = float(sale['total'])
        menu = sale['menu']
   
        total_sales += price
        menu_count[menu] = menu_count.get(menu, 0) + 1

        best_seller = max(menu_count, key=menu_count.get)

    summary_msg = (
            f"✨ *สรุปยอดขายประจำเมื่อวาน* ({yesterday}) ✨\n"
            f"----------------------------------\n"
            f"💰 ยอดรวมทั้งหมด: *{total_sales}* บาท\n"
            f"🏆 เมนูที่ขายดีที่สุดคือ: *{best_seller}* (ขายไปได้ {menu_count[best_seller]} ถ้วยแน่ะ!)\n"
            f"----------------------------------\n"
            f"วันนี้ก็สู้ๆ นะค๊าาา เฮงๆ รวยๆ เพี้ยง! 💖🦄"
        )

    send_telegram_msg(summary_msg)
    print(f"{summary_msg}")
    print("ส่งสรุปเรียบร้อยแล้วจ้าาา! ✨")



main()