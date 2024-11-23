"""Initiatives main application."""
import streamlit as st

from data.data_manager import DataManager
from app.pages.page_definer import PageDefiner
from app.pages.standard_page_content import StandardPageContent
from app.side_menu import SideMenu

if "role" not in st.session_state:
    st.session_state.role = None

pages = PageDefiner(st.session_state.role)

StandardPageContent().config().header()

DataManager().get_data()

SideMenu()

pages.pg.run()
