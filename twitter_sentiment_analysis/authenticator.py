import tweepy
import os
from dotenv import load_dotenv

project_folder = os.path.expanduser("~/Downloads/_python_twitter_sentimental_analysis/")  # adjust as appropriate
load_dotenv(os.path.join(project_folder, ".env"))

API_KEY = os.environ.get("API_KEY")
API_SECRET = os.environ.get("API_SECRET")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")


class TwitterAuthenticator:
    @staticmethod
    def authenticate():
        auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth, wait_on_rate_limit=True)

        return api
