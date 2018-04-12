# Sentiment-Analysis
Sentiment analysis on geo-spatial twitter data

The method used here is supervised learning using lexicon based approach.
In order to analyze the text, we used a python library called ‘TextBlob’.TextBlob provides a consistent API to perform natural language processing tasks such as Tokenization, Noun phrase extraction, Sentiment analysis etc. Textblob’s sentiment module allows us to determine the polarity and subjectivity of each tweet. 
We experimented with two types of models, pattern analyzer and naive bayes analyzer. The Pattern analyzer is based on the pattern library whereas the naive bayes analyzer is an NLTK classifier trained on a movie review corpus.  

After pre-processing the tweets, each tweet was read into a dataframe using pandas library in python. Every tweet is iterated through following three steps: 

1. Pattern analyzer
Pattern analyzer is the default analyzer of TextBlob. Itr returns a named tuple of the form:

Sentiment(polarity=0.0, subjectivity=0.0)

The polarity score ranges from  -1.0 to 1.0 and the subjectivity ranges from 0.0 to 1.0 where 0.0 is very objective and 1.0 is very subjective. Based on the polarity, whether it was 0, less than 0, or more than 0, the tweets are classified as neutral, negative and positive tweets respectively. 

2. Naive Bayes analyzer
The Naive Bayes analyzer is trained on a movie review corpus. It returns a named tuple of the form:

Sentiment(classification='neg', p_pos=0.4847806014974437, p_neg=0.5152193985025562)

This analyzer gives the positive probability score (p_pos) and negative probability score (n_neg). On the basis of this score, the machine decides the classification of each tweet. A major drawback of Naive Bayes is the time taken to execute, approaching 5 seconds per tweet. We observed that the Pattern analyzer outperformed Naive Bayes in terms of speed and accuracy.

3. Emoticon classifier
The emoticon classifier is built by employing a simple method of labelling the known emoticons and matching the pattern against the tweets. It is challenging to identify emoticons mainly because of encoding mismatches and varying notation for the same encoded emoticons. Although there are techniques to decode the emoticons such as scraping the utf-8 codes of emoticons and creating a dictionary to map them with the strange encoding caused by retrieving methods and platforms, this would be an extremely time consuming process. Therefore for this experiment, we manually collected as many emoticons that could be identified and grouped them into 3 sentiment categories - positive, negative and neutral. The tweets get checked against these 3 lists, thus capturing the emoticon sentiment contained in a particular tweet based on what category the emoticon falls into.
