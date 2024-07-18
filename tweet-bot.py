import tweepy
import tkinter as tk
from tkinter import Entry, Label, Button

# Functions to retrieve data from entry fields
def getd1():
    return d1.get()

def getd2():
    return d2.get()

def getd3():
    return d3.get()

def getd4():
    return d4.get()

def get_userdetails():
    consumer_key = getd1()
    consumer_secret = getd2()
    access_token = getd3()
    access_token_secret = getd4()
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        user = api.me()
        print(f"Welcome {user.name}")
    except tweepy.TweepError as e:
        print(e.response)
    
    return api

def getE1():
    return E1.get()

def getE2():
    return E2.get()

def getE4():
    return E4.get()

def getE5():
    return E5.get()

def getE6():
    return E6.get()

def getE7():
    return E7.get()

def mainFunction():
    api = get_userdetails()
    print("Tweet bot is activated")
    
    search = getE1()
    numberOfTweets = int(getE2())
    retweet = getE5().lower()
    favourite = getE6().lower()
    reply = getE4().lower()
    phrase = "This is done by a Tweeter bot"
    
    for tweet in tweepy.Cursor(api.search_tweets, search).items(numberOfTweets):
        try:
            if retweet == "yes":
                tweet.retweet()
                print('Retweeted the tweet')
            if favourite == "yes":
                tweet.favorite()
                print('Favourited the tweet')
            if reply == "yes":
                tweetId = tweet.id
                username = tweet.user.screen_name
                api.update_status(f"@{username} {phrase}", in_reply_to_status_id=tweetId)
                print(f"Replied with {phrase}")

        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

# Creating the GUI
root = tk.Tk()
root.title('Tweet bot')

l1 = Label(root, text="consumer_key")
l1.pack()
d1 = Entry(root, bd=5)
d1.pack()

l2 = Label(root, text="consumer_secret")
l2.pack()
d2 = Entry(root, bd=5)
d2.pack()

l3 = Label(root, text="access_token")
l3.pack()
d3 = Entry(root, bd=5)
d3.pack()

l4 = Label(root, text="access_token_secret")
l4.pack()
d4 = Entry(root, bd=5)
d4.pack()

submit = Button(root, text="Get User", command=get_userdetails)
submit.pack()

label1 = Label(root, text="Search")
label1.pack()
E1 = Entry(root, bd=5)
E1.pack()

label2 = Label(root, text="Number of Tweets")
label2.pack()
E2 = Entry(root, bd=5)
E2.pack()

label4 = Label(root, text="Reply? (yes/no)")
label4.pack()
E4 = Entry(root, bd=5)
E4.pack()

label5 = Label(root, text="Retweet? (yes/no)")
label5.pack()
E5 = Entry(root, bd=5)
E5.pack()

label6 = Label(root, text="Favorite? (yes/no)")
label6.pack()
E6 = Entry(root, bd=5)
E6.pack()

submit = Button(root, text="Submit", command=mainFunction)
submit.pack(side=tk.BOTTOM)

root.mainloop()
