import praw

reddit = praw.Reddit(
     client_id="1uGuV7ruCv9d7w",
     client_secret="8NRjudYtDAhdRbvl4_pjTcbjmXxsoQ",
     user_agent="console:wsbYOLO:1.0"
)

subreddit = reddit.subreddit("wallstreetbets")

for post in subreddit.top(limit=25):
    print(post.title,"\n********************************************\n")

    for comment in post.comments:
        if hasattr(comment,"body"):
            comLow = comment.body.lower()
            if(" bull" or " bear" or " yolo" or " bearish" or " bullish") in comLow:
                print(comment.body)
                print("-----")
