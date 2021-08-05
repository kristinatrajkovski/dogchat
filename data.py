from datetime import datetime

comment1 = {
    "Text": "What time are you going?",
    "Name": "Charlie",
    "Username": "char123",
    "Picture": "charlie.jpg",
    "DateTime": datetime(2021, 8, 5, 20, 4, 0)
}
comment2 = {
    "Text": "Idk maybe 3?",
    "Name": "Freddie",
    "Username": "freddie123",
    "Picture": "freddie.jpg",
    "DateTime": datetime(2021, 8, 5, 20, 25, 0)
}
comment3 = {
    "Text": "Woooo",
    "Name": "Charlie",
    "Username": "char123",
    "Picture": "charlie.jpg",
    "DateTime": datetime(2021, 8, 6, 20, 25, 0)
}
post1 = {
        "PostId": 1,
        "Name": "Freddie",
        "Username": "freddie123",
        "Text": "I can't wait to go to the park today",
        "Likes": ["charlie"],
        "Comments": [comment1, comment2],
        "DateTime": datetime(2021, 8, 5, 18, 4, 0),
        "Picture": "freddie.jpg"

    }
post2 = {
        "PostId": 2,
        "Name": "Charlie",
        "Username": "char123",
        "Text": "See you at the tournament!",
        "Likes": [],
        "Comments": [],
        "DateTime": datetime(2021, 8, 7, 18, 4, 0),
        "Picture": "charlie.jpg"

    }
post3 = {
        "PostId": 3,
        "Name": "Freddie",
        "Username": "freddie123",
        "Text": "Woooo!",
        "Likes": ["melba"],
        "Comments": [comment3],
        "DateTime": datetime(2021, 8, 6, 18, 4, 0),
        "Picture": "freddie.jpg"

    }

test_posts = {
    1: post1,
    2: post2,
    3: post3
}
freddie = {
    "Name" : "Freddie",
    "Username" : "freddie123",
    "Picture": "freddie.jpg",
    "Posts": [post1, post3],
    "Birthday": datetime(2019, 5, 21, 00, 00, 00),
    "Bio": "Hey, I'm Freddie, I'm an Alaskan Malamute and I am a very smart but a very bad dog!"
}
charlie = {
    "Name" : "Charlie",
    "Username" : "char123",
    "Picture": "charlie.jpg",
    "Posts": [post2],
    "Birthday": datetime(2017, 5, 5, 00, 00, 00),
    "Bio": "Hey, I'm Charlie, I'm a golden retriever and I enjoy sunny days!"
}
dogs = {
    "Freddie" : freddie,
    "Charlie" : charlie
}