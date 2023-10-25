class TwitterUserTimeLine:
    @staticmethod
    def posts(twitter_username, posts_count, api):
        posts = api.user_timeline(screen_name=twitter_username, count=posts_count, tweet_mode="extended")

        return posts
