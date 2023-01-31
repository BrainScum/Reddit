import praw
import config #config.py
import time
import os
"""import requests
import re
import sys"""

#https://www.reddit.com/prefs/apps
#https://www.reddit.com/r/test/comments/zdzwrt/test/

def bot_login():
    #logs in to the bot account
    r = praw.Reddit(username = config.username, password = config.password, client_id = config.client_id,
    client_secret = config.client_secret, user_agent = "creamcheeselover228 test bot")
    print("Successfully logged in!")

    return r

def run_bot(r, replied):
    #runs bot action - replying to comment with cream cheese in test sub
    #r.user.me() to specify bot account, config.username didn't work

    for comment in r.subreddit('test').comments(limit=25):
        if "cream cheese" in comment.body and comment.id not in replied and comment.author != r.user.me():
            print("\"cream cheese\" comment found in comment: " + comment.id)
            comment.reply("cream cheese? try [this](https://en.wikipedia.org/wiki/Cream_cheese).")

            replied.append(comment.id)

            with open ("creamcheesecomments.txt", "a") as f:
                f.write(comment.id + "\n")
            
    print("Sleeping for 10 seconds...")
    #sleeps for 10 seconds so that it doesn't spam and blow up my machine
    time.sleep(10)


def get_saved_comments():
    if not os.path.isfile("creamcheesecomments.txt"):
        comments = []
    else: 
        with open("creamcheesecomments.txt", "r") as f:
            comments = f.read()
            comments = comments.split("\n")
            comments = filter(None, comments)
    
    return comments

r = bot_login()
replied = get_saved_comments()
print(replied)

while True:
    run_bot(r, replied)



