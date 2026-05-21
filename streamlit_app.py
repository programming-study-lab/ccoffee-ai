import streamlit as st

pages = {
    "Your account": [
        st.Page("pages/2_Buy.py", title="Create your account"),
        st.Page("/pages/3_Caption.py", title="Manage your account"),
    ],
    "Resources": [
        st.Page("learn.py", title="Learn about us"),
        st.Page("trial.py", title="Try it out"),
    ],
}

pg = st.navigation(pages)
pg.run()