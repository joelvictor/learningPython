# Create a new Python script that prompts a user to enter in a potential Tweet and then print out whether the tweet is short enough to work (under 140 chars) or too long to post.
max_lenght = 140
tweet = input(f"Enter your tweet with max characters {max_lenght}: ")

number_characters = len(tweet)

msg = f"Tweet with lenght {number_characters} is "
if len(tweet) <= max_lenght:
    print(msg+"short enough to post.")
else:
    print(msg+"too long to post.")