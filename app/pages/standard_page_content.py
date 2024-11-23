"""Defines standard content for each page."""
import streamlit as st
from typing_extensions import Self

class StandardPageContent:
    def config(self: Self):
        st.set_page_config(initial_sidebar_state='collapsed')
        return self

    def header(self: Self):
        st.image("app/branding/logos/group_logo.png", width=150)
        st.title("Sedgley Charity Beer Festival")
        return self

    def day_selector(self: Self):
        col1, col2 = st.columns([0.3, 0.7])
        with col1:
            st.session_state.day = st.selectbox("Day", ["Friday & Saturday", "Friday", "Saturday"], label_visibility='hidden')
        return self

    def tabs(self: Self):
        self.people, self.finances, self.analysis = st.tabs(['👥 People', '💰  Finances', '📈  Analysis'])
        return self
