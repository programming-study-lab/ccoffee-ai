
try:
    import streamlit as st
    from src.views.SalesPageView import SalesPageView

    salesPageView = SalesPageView()
    salesPageView.run()
    # print(s)

except Exception as e:
    st.title(f"เกิดข้อผิดพลาดบางประการ ข้ออภัยในความไม่สะดวก: {e}")    
    pass    
    # st.title("เกิดข้อผิดบางประการกำลังดำเนินการแก้ไข")