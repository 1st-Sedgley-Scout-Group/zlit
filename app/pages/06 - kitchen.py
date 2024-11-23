"Kitchen"
import streamlit as st
import pandas as pd
from app.pages.standard_page_content import StandardPageContent

st.header("Kitchen")

content = StandardPageContent().day_selector().tabs()
