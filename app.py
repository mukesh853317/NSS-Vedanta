import streamlit as st
from database import init_db, get_connection
from modules.dashboard import render_dashboard
from modules.activities import render_activities
from modules.volunteers import render_volunteers
from modules.attendance import render_attendance
from modules.documents import render_documents
from modules.settings import render_settings

st.set_page_config(
    page_title="NSS Digital Management System",
    page_icon="🇮🇳",
    layout="wide",
    initial_sidebar_state="expanded",
)

init_db()

st.markdown("""
<style>
.main-title {font-size: 2rem; font-weight: 700; margin-bottom: 0;}
.sub-title {color: #666; margin-bottom: 1.5rem;}
.card {padding: 1rem; border: 1px solid #ddd; border-radius: 12px; background: #fff;}
</style>
""", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

with st.sidebar:
    st.title("🇮🇳 NSS Digital")
    st.caption("Version 1.0")
    st.divider()

    pages = ["Dashboard", "Activities", "Volunteers", "Attendance", "Documents", "Settings"]
    for p in pages:
        if st.button(p, use_container_width=True, type="primary" if st.session_state.page == p else "secondary"):
            st.session_state.page = p
            st.rerun()

    st.divider()
    st.caption("NSS Management & Documentation System")
    st.caption("Built with Streamlit + SQLite")

page = st.session_state.page

if page == "Dashboard":
    render_dashboard()
elif page == "Activities":
    render_activities()
elif page == "Volunteers":
    render_volunteers()
elif page == "Attendance":
    render_attendance()
elif page == "Documents":
    render_documents()
elif page == "Settings":
    render_settings()
