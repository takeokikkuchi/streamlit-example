"""
from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import schedule
import time
import snscrape.modules.twitter as sntwitter

# tweets_list1 = []
# # 実行job関数
# def job():
#     tweets_list1 = []
#     # Using TwitterSearchScraper to scrape data and append tweets to list
#     for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:jack').get_items()):
#         if i>100:
#             break
#         tweets_list1.append([tweet.date, tweet.id, tweet.content, tweet.username])
    
#     # Creating a dataframe from the tweets list above 
#     tweets_df1 = pd.DataFrame(tweets_list1, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
#     st.write(tweets_df1)

# schedule.every(2).minutes.do(job)

# #while True:
# for i in range(1,10):
#     schedule.run_pending()
#     time.sleep(1)

st.write("hello")
"""
# streamlit_app.py

import streamlit as st

def check_password():
    """Returns `True` if the user had a correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if (
            st.session_state["username"] in st.secrets["passwords"]
            and st.session_state["password"]
            == st.secrets["passwords"][st.session_state["username"]]
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store username + password
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show inputs for username + password.
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 User not known or password incorrect")
        return False
    else:
        # Password correct.
        return True

if check_password():
    st.write("Here goes your normal Streamlit app...")
    st.button("Click me")
