import datetime

import matplotlib.pyplot as plt
from wordcloud import WordCloud

plt.style.use("fivethirtyeight")


class Chart:
    def show(self):
        plt.show()

    def save(self, file_name):
        full_file_name = f"{datetime.date.today()}_{file_name}.png"
        plt.savefig(f"charts/{full_file_name}")

        return f"charts/{full_file_name}"


class WordsChart(Chart):
    def __init__(self, tweets, width=1000, height=1000, max_font_size=200):
        self.tweets = "".join(tweet for tweet in tweets)
        self.chart = WordCloud(width=width, height=height, max_font_size=max_font_size).generate(self.tweets)
        plt.imshow(self.chart, interpolation="bilinear")
        plt.axis("off")


class ScatterChart(Chart):
    def __init__(self, df):
        plt.figure("scatter", figsize=(14, 10))
        plt.title("Sentiment Analysis")
        plt.xlabel("Polarity")
        plt.ylabel("Subjectivity")

        for i in range(df.shape[0]):
            plt.scatter(df["Polarity"][i], df["Subjectivity"][i], color="Blue")


class PieChart(Chart):
    def __init__(self, sentiment_value_counts):
        plt.figure("pie", figsize=(14, 10))
        plt.title("Sentiment Analysis")
        sentiment_value_counts.plot(kind="pie")
