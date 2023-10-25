import requests
from operator import itemgetter

# Make an API call and store the response
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
req = requests.get(url)
print("Status code: ", req.status_code)

# Processing information about each submission
full_list_of_submissions = req.json()
top_30_submissions = []
for submission_id in full_list_of_submissions[:30]:
    # Make separate API call for each submission
    url = "https://hacker-news.firebaseio.com/v0/item/" + str(submission_id) + ".json"
    submission_requests = requests.get(url)
    # print("Status code: ", submission_requests.status_code)
    single_submission = submission_requests.json()

    one_of_top_30_submission = {
        "title": single_submission["title"],
        "link": ("https://news.ycombinator.com/item?id=" + str(submission_id)),
        "comments": single_submission.get(
            "descendants", 0
        ),  # dict.get method return value associate with
        # key (if exist), or value you provided
    }
    top_30_submissions.append(one_of_top_30_submission)

# Sorted articles via number of comments (revers order from most to least), need a itemgetter function to
# get comments from dict
top_30_submissions = sorted(
    top_30_submissions, key=itemgetter("comments"), reverse=True
)
top_10_most_comments_submissions = top_30_submissions[:10]

print("-" * 101)
for one_of_top_10_most_comments_submission in top_10_most_comments_submissions:
    print(f"{'Title:':<20} {one_of_top_10_most_comments_submission['title']}")
    print(f"{'Discussion link:':<20} {one_of_top_10_most_comments_submission['link']}")
    print(
        f"{'Number of comments:':<20} {one_of_top_10_most_comments_submission['comments']}"
    )
    print("-" * 101)
