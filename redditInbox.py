#!/usr/bin/python
import praw

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("ulcompsoc")

for item in reddit.inbox.all(limit=None):
    #print(repr(item))
    print(item.author)
    
    print(item.subject)
    print(item.body)
    print("-------\n")

##have all the main info now 

#get the message id too. 

#store all parsed message ids

#retrieve 20 messages 
# check last parsed date from a previous run of the program 

#better than checking against stored comment ids





