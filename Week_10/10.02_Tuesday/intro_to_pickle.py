#!/usr/bin/env python

# Introduction to Pickling
# Author: code adapted from Caroline Schmitt - DSI ATL by Noelle Brown - DSI DEN
# ---------------------------------------
# imports
import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegressionCV
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

"""
What is pickling?

If you're talking about food, pickling is a method of preserving food for the future. If you're talking about Python, pickling is a method of preserving objects for the future, including functions and classes. Since sklearn models are instances of classes, that means they can be pickled.

To pickle an object, it needs to be serialized. Serialization is when we transform an object into byte streams. (Byte streams are collections of bytes. One byte is made up of eight zeros or ones.) To unpickle an object so that it can be used in Python again, it needs to be deserialized.

If you've ever saved your progress in a video game, you've already serialized data without knowing it! A save file is your serialized save state. When you load the save, you deserialize the data so you can resume the game right where you were before you quit.

-----------------
Warning:

Just like you can't open a Pokemon: Red savefile in Pokemon: Sun, you have to unpickle an object in the same version of Python that you pickled it in.

Pickle objects can contain malevolent code. Never unpickle an object you don't trust!

-----------------
Why pickle?

Pickling makes a lot of sense any time you have a model you want to work with that you don't want to refit.

If you have a model that took twelve hours to fit, you might want to analyze its residuals, work with its coefficients, or make predictions off of it. But without Pickle, you'd need to refit the model every time you restarted your notebook. Pickling the model allows you to load the fitted model without needing to re-run the code where you fit it.

Note: pickling does not compress your model, meaning that some pickled models can end up being fairly large file sizes. (Think of K-nearest neighbors, which requires every data point to be stored inside the model.)
"""
# Pickling a simple datatype
# Before we pickle a full model, let's demonstrate pickling on a simple list.
# Create a list called `my_vegetables` that contains some strings:
my_vegetables =

"""
Write the pickled list to disk

Let's review this linkto go over why `with` is such a good tool for file operations:
https://www.pythonforbeginners.com/files/with-statement-in-python

Let's use `with` to write the list to disk as a `.pkl` file. We'll need to use `open`, pass in a file name, and also tell Python we're writing to the file, and writing as bytes. The pickle method we'll use is called `dump`.
"""
# Write the pickled list to disk
# "wb" means that you are writing to the file (w), and that you are writing in binary mode (b).


"""
Open the pickled list

Let's use `with` to open the pickled file and save it as a new variable, `list_from_pickle`. Remember to tell Python that we're reading from the file, and that we're reading in bytes. The pickle method we'll use is called `load`.
"""
# Open the pickled list



"""
Pickle a fitted pipeline

Here, we'll fit a pipeline to the Trump-Clinton corpus, then pickle the model. Then, we'll import the pickle in a new notebook to demonstrate how the model has been saved. Some code has been provided for you.
"""
# Import the data
# Here, the data is imported, and some elementary cleaning is performed:
df = pd.read_csv('data/trump_clinton_tweets.csv')
df = df[df['is_retweet'] == False][['text', 'handle']]
df.head(3)

#  Set up train and test


# Instantiate, fit, and score a pipeline


# Export the fitted pipeline to `my_pickles` as `pipeline.pkl`
# Just like before, we'll use a `with` statement


# Now, open the file called `read_a_pickle.py`.
