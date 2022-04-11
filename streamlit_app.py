"""
from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import schedule
import time
import snscrape.modules.twitter as sntwitter


st.write("hello")
"""
# streamlit_app.py

import streamlit as st

# Everything is accessible via the st.secrets dict:

st.write("DB username:", st.secrets["db_username"])
st.write("DB password:", st.secrets["db_password"])
st.write("My cool secrets:", st.secrets["my_cool_secrets"]["things_i_like"])

# And the root-level secrets are also accessible as environment variables:

import os

st.write(
    "Has environment variables been set:",
    os.environ["db_username"] == st.secrets["db_username"],
)
