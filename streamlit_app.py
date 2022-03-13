from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import schedule
import time
import snscrape.modules.twitter as sntwitter

tweets_list1 = []
# 実行job関数
def job():
    tweets_list1 = []
    # Using TwitterSearchScraper to scrape data and append tweets to list
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:jack').get_items()):
        if i>100:
            break
        tweets_list1.append([tweet.date, tweet.id, tweet.content, tweet.username])
    
    # Creating a dataframe from the tweets list above 
    tweets_df1 = pd.DataFrame(tweets_list1, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
    st.write(tweets_df1)

schedule.every(2).minutes.do(job)

#while True:
for i in range(1,10):
    schedule.run_pending()
    time.sleep(1)
