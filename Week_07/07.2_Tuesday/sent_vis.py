# Sentiment Analysis with VADER - visualization
# Author: code adapted from Caroline Schmitt - DSI ATL by Noelle Brown - DSI DEN
# ------------------------------------------------------------------
# imports
import pandas as pd
import sys
# plotting imports
import matplotlib.pyplot as plt
import seaborn as sns
# NLP imports
from nltk.sentiment.vader import SentimentIntensityAnalyzer
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

# ## Load in the text data:
tweets = pd.read_csv('~/your/file/path/data/trump_clinton_tweets.csv')

# remove retweets
tweets =
tweets =

# Format tweets for VADER:
# The `SentimentIntensityAnalyzer` will expect a list of strings.
corpus =

# Instantiate `SentimentIntensityAnalyzer`:
sia =

# create empty list

for tweet in corpus:
    # get sentiment scores

    # append text to scores

    # append text and sentiment scores to list


# create data frame of tweets and scores
df =

# Add original author:
df['author'] =

# Save the dataframe to use for modeling later
df.to_csv('~/your/file/path/data/tweets_with_scores.csv')

# Visualizing sentiments
# Let's do some EDA on the sentiments.
# Plot the average positivity and negativity for each politician:


# Plot a boxplot of compound scores for each politician:
#'compound' #takes pos, neut, & neg into account
# Code from Magnus - DEN
