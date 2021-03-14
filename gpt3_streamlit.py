import streamlit as st
import datetime 
import pandas as pd
import requests
import numpy as np
import matplotlib.pyplot as plt

#import joblib

from PIL import Image


st.set_page_config(page_title='Comodities Sentiment with GPT-3 by Finance Gurus')

st.write("""
# Comodities Sentiment with GPT-3 by Finance Gurus
""")

izbira_polja = ['Gold', 'Silver']
izbira = st.sidebar.selectbox("Select a comodity", izbira_polja, 0)
#returns the selection (0 or 1)

st.write('Choice: ', izbira)

st.write('Sentiment: [Buy, Hold, Sell]')

st.write('Finance Gurus: Rok & Latif ')