import pandas as pd
from textblob import TextBlob
# from textblob import Blobber
# from textblob.sentiments import NaiveBayesAnalyzer


df = \
    pd.read_csv('Tweets to execute.csv', encoding="ISO-8859-1")


pd.set_option('display.max_colwidth', -1)


emoji = []
emoji_sentiment = []

PA_sentiment = []
PA_polarity = []
PA_subjectivity = []


# NB_p_pos = []
# NB_n_neg = []
# NB_sentiment = []

happylist = [":)", ":D", ":*", ";)"]
sadlist = [":(", ":'("]
neutrallist = [":|"]
count=0
for index, row in df.iterrows():
    text = row['Tweet Text']
    emo = ""
    emo_sent = ""

    for x in happylist:
        if x in text:
            emo = emo + "," + x
            emo_sent = emo_sent + " positive,"

    for x in sadlist:
        if x in text:
            emo = emo + "," + x
            emo_sent = emo_sent + " negative,"

    for x in neutrallist:
        if x in text:
            emo = emo + "," + x
            emo_sent = emo_sent + " neutral,"

    emo = emo.lstrip(",")
    emo_sent = emo_sent.rstrip(",")
    emoji.append(emo)
    emoji_sentiment.append(emo_sent)


    # Pattern Analyzer

    blob2 = TextBlob(text)
    PA_polarity.append(blob2.sentiment.polarity)

    PA_subjectivity.append(blob2.sentiment.subjectivity)

    if (blob2.sentiment.polarity > 0):
        PA_sentiment.append("positive")
    elif (blob2.sentiment.polarity == 0):
        PA_sentiment.append("neutral")
    elif (blob2.sentiment.polarity < 0):
        PA_sentiment.append("negative")


    # Naive Bayes Analyzer

    # blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())

    # --overriding default analyzer

    # tb = Blobber(analyzer=NaiveBayesAnalyzer())
    #
    # a = tb(text).sentiment

    # a = blob.sentiment
    #
    # if a.__getattribute__("p_pos") > a.__getattribute__("p_neg"):
    #     NB_sentiment.append("positive")
    #
    # elif a.__getattribute__("p_pos") < a.__getattribute__("p_neg"):
    #     NB_sentiment.append("negative")
    # else:
    #     NB_sentiment.append("neutral")
    #
    # NB_p_pos.append(str(a.__getattribute__("p_pos")))
    #
    # NB_n_neg.append(str(a.__getattribute__("p_neg")))



    count = count + 1

    print(count)


df1 = pd.DataFrame(emoji, columns=['Emoji'])

df2 = pd.DataFrame(emoji_sentiment, columns=['Emoji Sentiment'])


df3 = pd.DataFrame(PA_sentiment, columns=['PA sentiment'])

df4 = pd.DataFrame(PA_polarity, columns=['PA polarity'])

df5 = pd.DataFrame(PA_subjectivity, columns=['PA subjectivity'])

# df6 = pd.DataFrame(NB_p_pos, columns=['NB p_pos'])
#
# df7 = pd.DataFrame(NB_n_neg, columns=['NB n_neg'])
#
# df8 = pd.DataFrame(NB_sentiment, columns=['NB sentiment'])


df6 = pd.concat([df1, df2, df3, df4, df5], axis=1)

df6.to_csv(r'NB_PA_sentiments_file1.csv', header='True', index='False', encoding='utf-8')
