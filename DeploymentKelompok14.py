# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 00:08:24 2021

@author: ASUS
"""

import streamlit as st
import numpy as np
import sklearn
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
from transformers import pipeline
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')


my_page = st.sidebar.radio('Halaman', ['Deployment', 'About'])

if my_page == 'Deployment':
    st.title('Sentiment Analysis: Tweet About Distance Learning')
    user_input = st.text_input("Masukkan Tweets: ")
    nltk.download("vader_lexicon")
    s = SentimentIntensityAnalyzer()
    score = s.polarity_scores(user_input)

    if score == 0:
        st.write("# Tweet Anda Dinilai Netral")
    elif score["neg"] != 0:
        st.write("# Tweet Anda Dinilai Negative")
    elif score["pos"] != 0:
        st.write("# Tweet Anda Dinilai Positive")
else:
    st.title('KELOMPOK 14 :')
    """
    Muhammad Imam Muzakki-195150207111025
    
    Fitra Bagus Arviyanto-195150207111026
    
    Muhammad Ihsan Saiful Kirom-195150200111026
    """


