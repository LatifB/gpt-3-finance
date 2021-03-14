import streamlit as st
import datetime 
import pandas as pd
import requests
import numpy as np
import matplotlib.pyplot as plt

#import joblib

from PIL import Image

from gpt_call import OpenAi
from yahoo_call import YahooCall

yahoo = YahooCall()
openai = OpenAi()

def scrape(Comodity="SILVER"):
    articles = yahoo.call(market=Comodity)
    return articles

def summarize(articles):
    summarized = [openai.sum_call(article)['choices'][0]['text'] for article in articles]
    return summarized

def sentiment(summarized):
    sentiments = []
    for summary in summarized:
        summary = f'summary: {summary}\nsentiment: '
        sentiments.append(openai.sent_call(summary))
    return sentiments

st.set_page_config(page_title='Comodities Sentiment with GPT-3 by Finance Gurus')

st.write("""
# Comodities Sentiment with GPT-3 by Finance Gurus
""")

izbira_polja = ['Gold', 'Silver']
izbira = st.sidebar.selectbox("Select a comodity", izbira_polja, 0)
#returns the selection (0 or 1)

commodity = 'GOLD' if izbira == 0 else 'SILVER'

scraped = scrape(commodity)
summarized = summarize(scraped)
summaries = '#'.join(summarized)
sentiments = sentiment(summaries)


for artice in summarized:
    st.write(f'article summary: {artice}')

for sentiment in sentiments:
    st.write(f'article sentiment: {sentiment}')

st.write('Choice: ', izbira)

st.write('Sentiment: [Buy, Hold, Sell]')

st.write('Finance Gurus: Rok & Latif ')