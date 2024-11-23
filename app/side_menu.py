"""Creates the sidemenu content."""
from typing_extensions import Self
import streamlit as st
from data.data_manager import DataManager

class SideMenu:
    def __init__(self: Self):
        self.footer()

    def footer(self: Self) -> None:
        st.sidebar.button("Refresh Data", on_click=DataManager()._refresh_data)
        st.sidebar.image("app/branding/logos/group_logo.png", width=150)
        st.sidebar.subheader("1st Sedgley Scout Group")
        st.sidebar.write("1stsedgleyscouts.org.uk")
        st.sidebar.write("#skillsforlife")
