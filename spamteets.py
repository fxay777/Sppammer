import tweepy
import tkinter as tk
from tkinter import Entry, Label, Button

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

def get_lab2():
    return m2.get()

def get_lab3():
    return m3.get()

def get_labd4():
    return m4.get()

def get_labd5():
    return m5.get()

def spamUser():
    api = get_userdetails()
    no = int(get_labd5())
    tweetId = get_lab3()
    username = get_lab2()
    message = get_labd4()

    for i in range(no):
        try:
            api.update_status(f"@{username} {message} {i+1}th time.", in_reply_to_status_id=tweetId)
            print(f"Replied with {message} {i+1}th time.")
        except tweepy.TweepError as e:
            print(e.reason)

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

submit_user = Button(root, text="Get User", command=get_userdetails)
submit_user.pack()

lab1 = Label(root, text="Spam a user")
lab1.pack()

lab2 = Label(root, text="tweetId")
lab2.pack()
m2 = Entry(root, bd=5)
m2.pack()

lab3 = Label(root, text="user name")
lab3.pack()
m3 = Entry(root, bd=5)
m3.pack()

lab4 = Label(root, text="Spam Message")
lab4.pack()
m4 = Entry(root, bd=5)
m4.pack()

lab5 = Label(root, text="Number of times")
lab5.pack()
m5 = Entry(root, bd=5)
m5.pack()

submit_spam = Button(root, text="Spam", command=spamUser)
submit_spam.pack(side=tk.BOTTOM)

root.mainloop()
