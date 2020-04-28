# Sentiment Analysis with VADER - modeling
# Author: code adapted from Caroline Schmitt - DSI ATL by Noelle Brown - DSI DEN
# ------------------------------------------------------------------
# imports
import pandas as pd
import sys
# NLP imports
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegressionCV
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from IPython.display import display
'''
VADER  (Valence Aware Dictionary and sEntiment Reasoner) is a sentiment analysis tool that was trained on social media posts. This notebook demonstrates using it on tweets by Hillary Clinton and Donald Trump during the 2016 presidential election. The dataset is from Kaggle.

Additional Resources:
- VADER Repo: https://github.com/cjhutto/vaderSentiment
- Dataset link: https://www.kaggle.com/benhamner/clinton-trump-tweets
- A paper on VADER: http://comp.social.gatech.edu/papers/icwsm14.vader.hutto.pdf
- A blog post on using VADER by Jodie Burchell: http://t-redactyl.io/blog/2017/04/using-vader-to-handle-sentiment-analysis-with-social-media-text.html

Citations:
Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for
Sentiment Analysis of Social Media Text. Eighth International Conference on
Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.
'''
# load dataset
df = pd.read_csv('~/your/file/path.csv')

# Modeling
# label whether or not the tweet is from Trump
# 'realDonaldTrump'
df['is_trump'] =

# X is tweet
X =
# Y is whether or not tweet is from Trump
y =
# Split into testing and training
X_train, X_test, y_train, y_test =

# Using Pipelines to make predictions on novel text
# Because a pipeline can wrap up count-vectorizing as well as the modeling step, we can use pipelines to make predictions about what a piece of text sounds like (https://iwl.me/):

def is_trump(words):
    # Set up a pipeline for this process to predict new tweets with count vectorizer & logistic regression (or any other model you would like to use)
    pipe =
    # fit pipeline

    # generate and return prediction

    return

# prompt user for input to function
words =
# print results
print()
