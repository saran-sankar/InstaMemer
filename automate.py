from getimage import getnewMeme
from postimage import postInstagramQuote

subreddits = ["dankmemes/top/?t=week", "dankmemes/hot/", "dankmemes/top/", "memes"]

posted = 0

for subreddit in subreddits:
    meme = getnewMeme("http://www.reddit.com/r/{}?t=day".format(subreddit))
    if meme != '':
        postInstagramQuote(meme)
        with open('./posted_log', 'a') as writer:
            writer.write(meme+'\n')
        posted = 1
        break
        
if posted == 0:
    print("No new memes to post! Try again later.")
