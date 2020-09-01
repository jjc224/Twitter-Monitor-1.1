  
#!/usr/bin/python3
# Author:   Joshua Coleman
# Filename: twittermonitor.py
# Purpose of the program: Program monitors tweets for provided handle in command line.

import sys
import time
import json
import requests
import GetOldTweets3 as got

def print_user_manual():
    print("-----\t---------------------------\t-----")
    print("*****\tTwitter Monitor Version 1.0\t*****")
    print("-----\t---------------------------\t-----")

def get_handle():
    # Check the count of arguments
    arg_count = len(sys.argv)

    # If missing handle, return error
    if not arg_count == 2:
        sys.stderr.write("\nMissing handle, try running the program again like this:\n"
            "$python3 twittermonitor.py <user_handle>")
        sys.exit(1)

    # Otherwise return the handle as string
    handle = None
    try:
        handle = str(sys.argv[1])
    except:
        sys.stderr.write("Missing handle, try running the program again like this:\n"
            "$python3 twittermonitor.py <user_handle>\n")
        sys.exit(1)

    return handle

def get_latest_tweets(handle, tweets_list):
    # Set criteria for tweet search with GetOldTweets3
    tweetCriteria = got.manager.TweetCriteria().setUsername(handle) \
                                               .setMaxTweets(5)
    # Get tweets
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)

    # Loop throughh new 5 tweets and add them to the list
    for tweet in tweets:
        tweet_formatted = "\n{content} - By {author} @ {time}".format(content=tweet.text, author=tweet.username, time=tweet.date)
        print(tweet_formatted)               # Print tweet
        tweets_list.append(tweet_formatted)  # Append new tweet to the list

def main():
    handle = None         # User provided as command line arg
    latest_tweets = None  # Latest 5 Tweets
    tweets_list = []      # List of all tweets collected during execution time for bounus task

    # 1. Print program instructions
    print_user_manual()

    # 2. Get handle
    handle = get_handle()

    # Repeat every 10 min
    while True:
        # 3. Get and print new 5 tweets and add them to the list
        get_latest_tweets(handle, tweets_list)
        # 4. Sleep for 10 min
        time.sleep(600) # 10 * 60sec

    # BONUS: Convert list to json and send via simple post request
    # tweets_json = json.dumps(tweets_list)
    # requests.post('https:localhost:8080', json=tweets_json)

    # Add simple POST request with 'requests'


if __name__ == "__main__":
    main()
