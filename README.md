---
title: ccoffee-ai
emoji: 🚀
colorFrom: red
colorTo: red
sdk: docker
app_port: 8501
tags:
- streamlit
pinned: false
short_description: Streamlit template space
---

## URL หน้าเว็บ Huggingface
https://huggingface.co/spaces/ccoffee2026/shop

## URL หน้าเว็บ shop.ccoffee.me
https://shop.ccoffee.me/

## PIVOT
https://github.com/programming-study-lab/ccoffee-ai/blob/main/PIVOT.md

## สำหรับเข้าสู่ระบบ
- User Name: demo-day
- Password: password

## Tech Stack
- GitHub
- Python
- Streamlit
- Google Sheets API
- Google Gemini API

## Reflection
1) สิ่งที่ทำได้ดีที่สุดใน 5 session นี้คืออะไร <br>
ตอบ 1) Check-in หน้าห้อง + ส่ง Agent Harness Report (ฉบับเขียนมือ) ให้ผู้สอน
    2) Final Exam — Written On-site (handwritten) 1 ชั่วโมง closed-book
    3) Reflection brief <br>
2) Pivot จาก MilkLab° เป็น domain ของตัวเอง ส่วนไหนยากที่สุด <br>
ตอบ 1) หาไอเดียธุรกิจ 
    2) การใช้งาน Streamlit โดยเฉพาะ การ ใช้งาน st.navigation
    3) การใช้งาน Library "bcrypt" <br>
3) Feedback จาก cohort ที่จะเอาไปใช้ มีอะไรบ้าง <br>
ตอบ "ควรเพิ่มระบบจัดการ Context เพื่อให้บอทจดจำข้อความสนทนาได้" <br>
4) จะนำ skill ที่ได้ไปใช้กับโปรเจกต์/ธุรกิจอะไรต่อไป <br>
ตอบ จะนำไปใช้ประกอบอาชีพ

# วัตถุประสงค์ 
โปรเจค ร้านอาหาร เสบียงเรียน (Study Fuel) เพื่อการศึกษา การใช้งาน AI ช่วยพัฒนา Web Application สำหรับ ธุรกิจแบบ  Solopreneurs
# สิ่งที่คาดหวัง
การนำ AI มาประยุกค์ใช้ในงาน Web Application สำหรับ ธุรกิจแบบ Solopreneurs
# สิ่งที่ได้เรียนรู้
- Session 1: สร้าง Caption โดยใช้ AI
- Session 2: 
    1) การใช้งาน GitHub Actions Workflow
    2) บันทึกข้อมูลใน Google Sheets โดยใช้ API
    3) การใช้งาน Telegram Bot
    4) การใช้งาน .gitignore
- Session 2.5:
    1) การใช้งาน Agent Harness
    2) การใช้งาน Branch ของ Git
    3) การติดตั้ง Library จาก file requirements.txt
    4) วิธีการใช้ Pull Request
- Session 3:
    1) การใช้งาน RAG Chatbot
    2) การ Deploy บน HuggingFace Spaces
- Session 4:
    1) ผูก Namecheap domain กับ HuggingFace Space
    2) ทำงานร่วมกับผู้อื่นภายในกลุ่ม
- Session 5:
    1) ได้เรียนรู้งานจากกลุ่มอื่น

## Mini Project Function
1. มี AI ผู้ช่วยตอบคำถามเกี่ยวกับร้านอาหาร เสบียงเรียน (Study Fuel)
2. ระบบสั่งซื้อสินค้าจากหน้าเว็บ
3. ระบบตรวจสอบสิทธิ์การใช้งาน
4. ระบบเพิ่มพนักงาน
5. ระบบสร้าง Caption
6. สามารถออกจากระบบ


## วิธี run local
# บน Windows OS
```bash
> git clone https://github.com/programming-study-lab/ccoffee-ai.cd ccoffee-ai
> cd ccoffee-ai
> python -m venv venv
> venv/Scripts/pip install -r .\requirements.txt

> venv/Scripts/Activate.ps1  หรือ venv/Scripts/activate

(venv)> streamlit run app.py
```
```bash
สร้างไฟล์ .env
    # Gemini
    GEMINI_MAX_OUTPUT_TOKENS=<จำนวน Token สูงสุดที่ต้องการใช้>
    GEMINI_MODEL= <โมเดล Gemini>
    GEMINI_API_KEY= <api_ของ_Gemini>
    
    # Telegram
    TELEGRAM_BOT_TOKEN= <telegram_token>
    TELEGRAM_CHAT_ID= <id_chat_telegram>

    # Google Sheets services
    GOOGLE_SERVICE_ACCOUNT_FILE= <path_file>
    SALES_GOOGLE_SHEET_ID= <id ของ Google Sheet สำหรับบันทึกคำสั่งซื้อ>
    MENU_GOOGLE_SHEET_ID= <id ของ Google Sheet สำหรับบันทึกเมนู>
    ADMIN_GOOGLE_SHEET_ID= <id ของ Google Sheet สำหรับบันทึกข้อมูลของผู้ดูแลระบบ>

    # Admin Key (สำหรับการทดสอบ)
    ADMIN_KEY= <ใช้สำหรับตรวจสอบ Admin (แบบทดสอบ)>

สร้างไฟล์ service-account.json
    ข้อมูลในไฟล์ คือ service account จาก Google
```

## Session 1: Caption Generator
# สิ่งที่ต้องเตรียมก่อนเริ่ม
- [ / ] บัญชี GitHub (สมัครฟรีที่ github.com)
- [ / ] ยืนยันสถานะนักศึกษากับ GitHub Education แล้ว (education.github.com)
- [ / ] Activate AI coding assistant (Copilot ถ้ามี / Gemini Code Assist ถ้าไม่มี — ดู Quickstart)
- [ / ] Browser Chrome หรือ Edge อัปเดตเป็นเวอร์ชันล่าสุด

# Checklist ก่อนออกจาก Session
- [ / ] <ใช้ชื่ออื่น> Repository milk-lab-ai มีอยู่บน GitHub (ใช้ชื่ออื่นคือ "ccoffee-ai" เพราะเข้าใจผิดว่าให้ทำธุรกิจอื่น)
- [ / ] caption.py รันได้และ output caption 3 แบบ
- [ / ] ไฟล์ .env ไม่ถูก push ขึ้น GitHub
- [ / ] ไฟล์ .gitignore มี .env อยู่แล้ว

## Session 2: Sales Logger + Demi Alert
# สิ่งที่ต้องเตรียมก่อนเริ่ม
- [ / ] <ใช้ชื่ออื่น> Repository milk-lab-ai จาก Session 1 ที่ push ขึ้น GitHub แล้ว
- [ / ] บัญชี Google ที่ใช้ใน Session 1
- [ / ] Telegram account (ถ้ายังไม่มี ให้ download app และสมัครก่อน)

# Checklist ก่อนออกจาก Session
- [ / ] Branch feature/sales-logger มีและ merge เข้า main แล้ว
- [ / ] sales_logger.py บันทึกข้อมูลลง Google Sheets ได้
- [ / ] morning_report.py ส่ง Telegram ได้
- [ / ] GitHub Actions workflow รันได้ (มีเครื่องหมาย ✅)
- [ / ] ไม่มีไฟล์ .json หรือ .env ถูก push ขึ้น GitHub 

## Session 2.5: Agent Harness
- [ / ] agent_tools.py มี guardrails ที่ reject ข้อมูลผิด
- [ / ] agent_harness.py รับคำสั่งภาษาไทยและเรียก tool ได้ถูกต้อง
- [ / ] agent_trace.log บันทึก log ทุก step
- [ x ] <มี Pull Request ที่ Demo Day> Pull Request เปิดแล้วและมีคนมา review 

## Session 3: Demi RAG Chatbot
- [ / ] rag_engine.py โหลด chunk embed และค้นหาได้ถูกต้อง
- [ / ] app.py ตอบจาก knowledge base (ไม่แต่งข้อมูลเอง)
- [ / ] Deploy ขึ้น HuggingFace Spaces มี URL ใช้งานได้จริง
- [ / ] ทดสอบด้วยคำถาม 5 ข้อ ตอบถูกทุกข้อ

## Session 4: Pivot Day + Project Clinic
# UI / UX
- [ / ] ชื่อ app และ branding สอดคล้องกับ domain ใหม่
- [ / ] ภาษาที่ใช้เหมาะกับ persona ลูกค้า (วัยรุ่น vs. ผู้สูงอายุ ใช้คำต่างกัน)
- [ / ] มี error message ที่อ่านเข้าใจง่ายเมื่อเกิดปัญหา
- [ / ] หน้าตา Streamlit สะอาด ไม่มี debug output โผล่
# Code Quality
- [ / ] ลบ print() ที่ใช้ debug ออกแล้ว
- [ / ] ไม่มี hard-coded API key ในโค้ด
- [ / ] requirements.txt ครบถ้วน
# README.md
- [ / ] อธิบายว่าระบบทำอะไร สำหรับ domain ของนักศึกษา (ไม่ใช่ MilkLab°)
- [ / ] มี link ไปยัง live demo URL
- [ / ] มีวิธีรันในเครื่องท้องถิ่น (local setup)
- [ / ] ใส่ link ไปยัง PIVOT.md เพื่อให้ recruiter เห็น thinking process

## Session 5: Demo Day
# ก่อน 23 พ.ค. (เปิด window Cohort Round)
- [ / ] Demo URL ทำงานได้
- [ / ] Self-Check checklist ใน README ครบ
- [ / ] เตรียม hook 30 วินาทีที่จะใช้เปิด demo
- [ / ] Final Project submit ใน Class.ecp ก่อน 25 พ.ค. 23:59
- [ / ] ทบทวน scope Final Exam (4 ส่วน: Concepts / Tool design / RAG / Applied scenario)
- [ / ] ช่วง 23–26 พ.ค. (Cohort Round — กลุ่มนัดกันเอง, แนะนำ จ. 25 พ.ค.)


# นัด Teams meeting ของ cohort + เข้า meeting ตามนัด
- [ / ] Demo + ตอบ Q&A กับสมาชิก cohort
- [ / ] ทำ Class.ecp Feedback Cohort Round Peer Eval ให้สมาชิก cohort ครบ ก่อน 26 พ.ค. 23:59
- [ / ] (Anchor/scribe) Submit Cohort Top Pick Declaration ระบุ Top Pick + runner-up ก่อน 26 พ.ค. 23:59

# วัน 27 พ.ค. (ห้อง 311)
- [ / ] เตรียม Agent Harness Report ฉบับเขียนมือ เอามาส่งวันงาน
- [ / ] Check-in 12:45 + ส่ง Agent Harness Report ที่ผู้สอน
- [ x ] <คนอื่นนำเสนอ> (Top Pick) เตรียม slides/script 90 วินาที + ขึ้นพูดตอน 13:10
- [ x ] <ไม่มี Vote> Vote 5 รางวัลรวม (13:40–14:00)
- [ / ] สอบ Final Exam ข้อเขียน 14:25–15:25 (closed-book — เก็บมือถือ/laptop/ตำรา)
- [ / ] เขียน Reflection ใน README (ส่งภายใน 29 พ.ค. 23:59)

## Demo Day Self-Check
- [ / ] Deploy URL ใช้งานได้ (เปิดทดสอบล่าสุด: 28/05/2569)
- [ / ] ไม่มี `.env` หรือ `*.json` ใน git history
- [ / ] PIVOT.md ครบ 3 ข้อ
- [ / ] README อธิบายระบบของ domain ตัวเอง (ไม่ใช่ MilkLab°)
- [ / ] knowledge base, prompt, UI ปรับเป็น domain ใหม่หมดแล้ว

## Directory Tree
```base
.
├── CNAME
├── Dockerfile
├── PIVOT.md
├── README.md
├── agent_harness.py
├── agent_tools.py
├── agent_trace.log
├── app.py
├── caption.py
├── knowledge
│   └── ccoffee_kb.txt
├── morning_report.py
├── pages
│   ├── 1_Ccoffee Chat.py
│   ├── 2_Buy.py
│   ├── 3_Caption.py
│   ├── 4_Login.py
│   ├── 98_Register.py
│   └── 99_Logout.py
├── rag_engine.py
├── requirements.txt
├── sales_logger.py
├── service-account.json
├── sheets_client.py
├── src
│   ├── controllers
│   │   ├── CaptionController.py
│   │   ├── ChatBotController.py
│   │   ├── HomeController.py
│   │   ├── LogoutController.py
│   │   └── SalesPageController.py
│   ├── databases
│   │   ├── AdminGoogleSheetDatabase.py
│   │   ├── MenuGoogleSheet.py
│   │   └── SalesGoogleSheetDatabase.py
│   ├── helpers
│   │   ├── AlertHelper.py
│   │   └── Router.py
│   ├── models
│   │   ├── MenuModel.py
│   │   └── SalesModel.py
│   ├── services
│   │   ├── AdminService.py
│   │   ├── MenuService.py
│   │   └── SalesService.py
│   └── views
│       ├── CaptionPageView.py
│       ├── HomeView.py
│       ├── LoginView.py
│       ├── LogoutView.py
│       ├── RegisterView.py
│       └── SalesPageView.py
├── streamlit_app.py
├── test.py
└── คู่มือติดตั้ง.txt
```