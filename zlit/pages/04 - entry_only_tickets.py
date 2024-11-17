import streamlit as st

st.header("Entry Only Tickets")

col1, col2 = st.columns([0.3, 0.7])
with col1:
    day = st.selectbox("Day", ["Friday & Saturday", "Friday", "Saturday"], label_visibility='hidden')

people, finances, analysis = st.tabs(['👥 People', '💰  Finances', '📈  Analysis'])
