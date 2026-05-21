try:
    import streamlit as st

    class AlertHelper:
        title = ''

        def __init__(self, title, message):
            title = title
            self.message = message

        @st.dialog("f{title}")
        def showPopUp(self):
            st.write(f"{self.message}")
            if st.button("ตกลง"):
                st.rerun()

except Exception as e:
    st.title("เกิดข้อผิดพลาด")


