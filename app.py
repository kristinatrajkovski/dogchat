from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def feed():
    post1 = {
        "Name": "Freddie",
        "Username0": "freddie123",
        "Text": "I can't wait to go to the park today",
        "LikesN": 10,
        "CommentsN": 5,
        "DateTime": datetime(2021, 8, 5, 18, 4, 0),
        "Picture": "freddie.jpg"

    }
    post2 = {
        "Name": "Freddie",
        "Username0": "freddie123",
        "Text": "See you at the tournament!",
        "LikesN": 10,
        "CommentsN": 5,
        "DateTime": datetime(2021, 8, 7, 18, 4, 0),
        "Picture": "freddie.jpg"

    }
    post3 = {
        "Name": "Freddie",
        "Username0": "freddie123",
        "Text": "Woooo!",
        "LikesN": 10,
        "CommentsN": 5,
        "DateTime": datetime(2021, 8, 6, 18, 4, 0),
        "Picture": "freddie.jpg"

    }
    test_posts = [post1, post2, post3]
    return render_template('index.html', posts = test_posts)