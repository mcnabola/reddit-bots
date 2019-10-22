#!/usr/bin/python
import praw
import pdb
import re
import os
#what are the 3 other imports needed for.

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("ulcompsoc")

if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_replied_to.txt") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))
      
subreddit = reddit.subreddit("ulcompsoc")
for submission in subreddit.hot(limit=2):
    if submission.id not in posts_replied_to:
        if re.search("compsoc loves python", submission.title, re.IGNORECASE):
            submission.reply("Skynet0001 says Hello!")
            print("Bot replying to : ", submission.title)
            posts_replied_to.append(submission.id)

with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")


