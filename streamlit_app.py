import streamlit as st

if "role" not in st.session_state:
    st.session_state.role = None

ROLES = [None, "Organising Team", "1st Sedgley", "Scout Leaders", "Explorers"]


def login():

    st.header("Log in")
    role = st.selectbox("Choose your role", ROLES)

    if st.button("Log in"):
        st.session_state.role = role
        st.rerun()


def logout():
    st.session_state.role = None
    st.rerun()


role = st.session_state.role

logout_page = st.Page(logout, title="Log out", icon=":material/logout:")

summary = st.Page(
    "zlit/pages/01 - summary.py",
    title="Summary",
    icon=":material/help:",
    default=(role in ["Organising Team", "1st Sedgley"]),
)

entry = st.Page(
    "zlit/pages/02 - entry_tickets.py",
    title="Entry Tickets",
    icon=":material/help:",
)

topup = st.Page(
    "zlit/pages/03 - topup_tokens.py",
    title="Top-up Tokens",
    icon=":material/help:",
)

entry_only = st.Page(
    "zlit/pages/04 - entry_only_tickets.py",
    title="Entry Only Tickets",
    icon=":material/help:",
)

bbq = st.Page(
    "zlit/pages/05 - bbq.py",
    title="BBQ",
    icon=":material/help:",
    default=(role == "Scout Leaders"),
)

kitchen = st.Page(
    "zlit/pages/06 - kitchen.py",
    title="Kitchen",
    icon=":material/help:",
    default=(role == "Explorers"),
)

account_pages = [logout_page]
summary_pages = [summary]
ticket_pages = [entry, topup, entry_only]
bbq_pages = [bbq]
kitchen_pages = [kitchen]

st.title("Sedgley Charity Beer Festival")

page_dict = {}
if st.session_state.role == "Organising Team":
    page_dict[""] = summary_pages
    page_dict["Tickets"] = ticket_pages
    page_dict["Food"] = bbq_pages + kitchen_pages
if st.session_state.role == "1st Sedgley":
    page_dict[""] = summary_pages
    page_dict["Tickets"] = ticket_pages
    page_dict["Food"] = bbq_pages
if st.session_state.role == "Scout Leaders":
    page_dict[""] = bbq_pages
if st.session_state.role == "Explorers":
    page_dict[""] = kitchen_pages

if len(page_dict) > 0:
    pg = st.navigation(page_dict | {"Account": account_pages})
else:
    pg = st.navigation([st.Page(login)])

pg.run()
