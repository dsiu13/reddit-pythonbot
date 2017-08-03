import praw
import config
import time
import os
import requests

def bot_login():
    print("Logging In..")
    r = praw.Reddit(username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = "test bot plz ignore")
    print("Login Succesful")

    return r

def run_bot(r, comments_replied_to):
    for comment in r.subreddit('test').comments(limit=25):
        if "bot" in comment.body and comment.id not in comments_replied_to and not comment.author == r.user.me():
            print ("String Found")
            # comment.reply("I'm Also a Bot")
            # joke = requests.get('http://api.icndb.com/jokes/random').json()['value']['joke']
            # comment.reply = joke
            comments_replied_to.append(comment.id)

            with open ("comments_replied_to.txt", "a") as f:
                f.write(comment.id + "\n")

    print('Sleep Time')
    time.sleep(10)

def get_saved_comments():
    if not os.path.isfile("comments_replied_to.txt"):
        comments_replied_to = []
    else:
        with open("comments_replied_to.txt", "r") as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split("\n")
            comments_replied_to = list(filter(None, comments_replied_to))

    return comments_replied_to

r = bot_login()
comments_replied_to = get_saved_comments()

while True:
    run_bot(r, comments_replied_to)
