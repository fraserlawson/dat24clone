import sys

import numpy as np
from IPython.core.display import Image

import praw


reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent,
    username=username,
    password=password,
)
subreddit = reddit.subreddit("showerthoughts")

# go by timespan - 'hour', 'day', 'week', 'month', 'year', 'all'
# might need to go longer than an hour to get entries...
top_submissions = subreddit.top('hour')

n_sub = int(sys.argv[1]) if len(sys.argv) > 1 else 1

i = 0
while i < n_sub:
    top_submission = next(top_submissions)
    i += 1

top_post = top_submission.title

upvotes = []
downvotes = []
contents = []

for sub in top_submissions:
    try:
        ratio = sub.upvote_ratio
        ups = int(round((ratio*sub.score)/(2*ratio - 1))
                  if ratio != 0.5 else round(sub.score/2))
        upvotes.append(ups)
        downvotes.append(ups - sub.score)
        contents.append(sub.title)
    except Exception as e:
        continue
votes = np.array( [ upvotes, downvotes] ).T

