import re

import pandas as pd
from textblob import TextBlob


class Analyzer:
    def __init__(self, posts):
        self.df = pd.DataFrame([tweet.full_text for tweet in posts], columns=["Tweets"])

        self.df["Tweets"] = self.df["Tweets"].apply(self._clean_txt)
        self.df["Subjectivity"] = self.df["Tweets"].apply(self._get_subjectivity)  # 0 (fact) - 1 (opinion)
        self.df["Polarity"] = self.df["Tweets"].apply(self._get_polarity)
        self.df["Analysis"] = self.df["Polarity"].apply(self._get_analysis)
        self.sentiment_value_counts = self.df["Analysis"].value_counts()

        self.pos_df = self._show_only_tweets_with_given_sentiment("Positive")
        self.neg_df = self._show_only_tweets_with_given_sentiment("Negative")
        self.neut_df = self._show_only_tweets_with_given_sentiment("Neutral")

        self.pos_tweets_num = self._show_how_many_tweets_with_given_sentiment("Positive")
        self.neg_tweets_num = self._show_how_many_tweets_with_given_sentiment("Negative")
        self.neut_tweets_num = self._show_how_many_tweets_with_given_sentiment("Neutral")

        self.pos_tweets_num_as_percent = self._show_how_many_tweets_with_given_sentiment_as_percentage("Positive")
        self.neg_tweets_num_as_percent = self._show_how_many_tweets_with_given_sentiment_as_percentage("Negative")
        self.neut_tweets_num_as_percent = self._show_how_many_tweets_with_given_sentiment_as_percentage("Neutral")

    def _clean_txt(self, text):
        text = re.sub(r"@[A-Za-z0-9]+", "", text)
        text = re.sub(r"#", "", text)
        text = re.sub(r"RT[\s]+", "", text)
        text = re.sub(r"https?:\/\/\/S+", "", text)

        return text

    def _get_subjectivity(self, text):
        return TextBlob(text).sentiment.subjectivity

    def _get_polarity(self, text):
        return TextBlob(text).sentiment.polarity

    def _get_analysis(self, score):
        if score == 0:
            return "Neutral"
        elif score < 0:
            return "Negative"
        else:
            return "Positive"

    def _show_only_tweets_with_given_sentiment(self, sentiment):
        self._raise_exception(sentiment)

        index_to_delete = {"Positive": [], "Negative": [], "Neutral": []}
        for i in range(self.df.shape[0]):
            index_to_delete[sentiment].append(i) if (self.df["Analysis"][i] != sentiment) else None

        return self.df.drop(index=index_to_delete[sentiment], inplace=False)

    def _show_how_many_tweets_with_given_sentiment(self, sentiment):
        self._raise_exception(sentiment)

        return self.df[self.df.Analysis == sentiment].shape[0]

    def _show_how_many_tweets_with_given_sentiment_as_percentage(self, sentiment):
        self._raise_exception(sentiment)
        tweets_with_given_sentiments = self._show_how_many_tweets_with_given_sentiment(sentiment)
        total = self.df.shape[0]

        return round(tweets_with_given_sentiments / total * 100, 2)

    def _raise_exception(self, sentiment):
        if sentiment not in ["Positive", "Negative", "Neutral"]:
            raise Exception("Something went wrong")

    def sort(self, reverse=False):
        if reverse is True:
            self.df = self.df.sort_values(by=["Polarity"], ascending=False)
        else:
            self.df = self.df.sort_values(by=["Polarity"])
