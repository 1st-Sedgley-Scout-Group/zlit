"""Manages getting Zettle data."""
import os

import pandas as pd
import pyzettle as pz
import streamlit as st
from dotenv import load_dotenv


class DataManager:

    @staticmethod
    @st.cache_data(ttl=600, max_entries=1)
    def get_data() -> pd.DataFrame:
        load_dotenv()
        return pz.GetPayments(
        client_id=os.getenv("CLIENT_ID"),
        api_key=os.getenv("API_KEY"),
        ).data


    @staticmethod
    def _refresh_data():
        st.cache_data.clear()
        DataManager().get_data()
