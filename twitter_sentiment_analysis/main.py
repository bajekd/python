import argparse

from analyzer import Analyzer
from authenticator import TwitterAuthenticator
from charts import PieChart, ScatterChart, WordsChart
from pdf_generator import PDFGenerator
from posts import TwitterUserTimeLine


def main():
    parser = argparse.ArgumentParser(prog="twitter_sentiment_analysis")
    parser.add_argument("user_name", type=str, help="name of twitter user")
    parser.add_argument("number_of_tweets", type=int, help="number of tweets from specified user")
    args = parser.parse_args()

    api = TwitterAuthenticator.authenticate()
    posts = TwitterUserTimeLine.posts(args.user_name, args.number_of_tweets, api)
    analysis = Analyzer(posts)

    path_to_worlds_cloud = WordsChart(analysis.df["Tweets"]).save("words_cloud")
    path_to_scatter_chart = ScatterChart(analysis.df).save("scatter")
    path_to_pie_chart = PieChart(analysis.sentiment_value_counts).save("pie_chart")

    report = PDFGenerator(args.number_of_tweets, args.user_name)
    report.save(path_to_worlds_cloud, path_to_scatter_chart, path_to_pie_chart)


if __name__ == "__main__":
    main()
