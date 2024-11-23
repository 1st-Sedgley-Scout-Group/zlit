"""Manages users behaviors of the application."""
from typing_extensions import Self
import streamlit as st

ROLES = [None, "Organising Team", "1st Sedgley", "Scout Leaders", "Explorers"]

class UserManager:

    def login():
        st.header("Log in")
        role = st.selectbox("Choose your role", ROLES)

        if st.button("Log in"):
            st.session_state.role = role
            st.rerun()

    def logout():
        st.session_state.role = None
        st.rerun()
