try:
    import streamlit as st

    class AlertHelper:

        def __init__(self, message):
            self.message = message

        @st.dialog(f"แจ้งเตือน")
        def showPopUp(self):
            st.write(f"{self.message}")
            if st.button("ตกลง"):
                st.rerun()

except Exception as e:
    st.title(f"เกิดข้อผิดพลาด {e}")


