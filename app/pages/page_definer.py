"""Defines the pages, page groups and what pages are visible for each user."""
from typing_extensions import Self
import streamlit as st
from app.user_manager import UserManager

class PageDefiner:
    def __init__(self: Self, role):
        self.locate_pages(role)
        self.group_pages()
        self.select_pages()

    def locate_pages(self: Self, role: str):
        self.logout_page = st.Page(UserManager.logout, title="Log out", icon=":material/logout:")

        self.home = st.Page(
            "app/pages/09 - home.py",
            title="Home",
            icon=":material/help:",
        )

        self.summary = st.Page(
            "app/pages/01 - summary.py",
            title="Summary",
            icon=":material/help:",
            default=(role in ["Organising Team", "1st Sedgley"]),
        )

        self.entry = st.Page(
            "app/pages/02 - entry_tickets.py",
            title="Entry Tickets",
            icon=":material/help:",
        )

        self.topup = st.Page(
            "app/pages/03 - topup_tokens.py",
            title="Top-up Tokens",
            icon=":material/help:",
        )

        self.entry_only = st.Page(
            "app/pages/04 - entry_only_tickets.py",
            title="Entry Only Tickets",
            icon=":material/help:",
        )

        self.bbq = st.Page(
            "app/pages/05 - bbq.py",
            title="BBQ",
            icon=":material/help:",
            default=(role == "Scout Leaders"),
        )

        self.kitchen = st.Page(
            "app/pages/06 - kitchen.py",
            title="Kitchen",
            icon=":material/help:",
            default=(role == "Explorers"),
        )

        return self

    def group_pages(self: Self):

        self.account_pages = [self.logout_page, self.home]
        self.summary_pages = [self.summary]
        self.ticket_pages = [self.entry, self.topup, self.entry_only]
        self.bbq_pages = [self.bbq]
        self.kitchen_pages = [self.kitchen]

        return self

    def select_pages(self: Self):
        self.page_dict = {}

        if st.session_state.role == "Organising Team":
            self.page_dict[""] = self.summary_pages
            self.page_dict["Tickets"] = self.ticket_pages
            self.page_dict["Food"] = self.bbq_pages + self.kitchen_pages

        if st.session_state.role == "Organising Team":
            self.page_dict[""] = self.summary_pages
            self.page_dict["Tickets"] = self.ticket_pages
            self.page_dict["Food"] = self.bbq_pages + self.kitchen_pages

        if st.session_state.role == "1st Sedgley":
            self.page_dict[""] = self.summary_pages
            self.page_dict["Tickets"] = self.ticket_pages
            self.page_dict["Food"] = self.bbq_pages

        if st.session_state.role == "Scout Leaders":
            self.page_dict[""] = self.bbq_pages

        if st.session_state.role == "Explorers":
            self.page_dict[""] = self.kitchen_pages

        if len(self.page_dict) > 0:
            self.pg = st.navigation(self.page_dict | {"Account": self.account_pages})
        else:
            self.pg = st.navigation([st.Page(UserManager.login)])


        return self
