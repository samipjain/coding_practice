import tweepy
import csv

consumeer_key = "TE0lGIzIVsaddkBxM34cjyrdg"
consumer_secret_key = "ClJdwa6pva3YUwvGii404dCLazBLL7f6rRH2Z5JUao9owZKAgC"
access_token = "290463860-zQPXrFkhRqEQImPcf6C48ftiyXoron4TDRIFkEtY"
access_token_secret = "ISKB8ZELIMjIVinwX1eb36hxS4Buvckh6zw6uDifP9rjY"

auth = tweepy.OAuthHandler(consumeer_key, consumer_secret_key)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

csvFile = open('loneliness.csv', 'w')
csvWriter = csv.writer(csvFile)

public_tweets = api.search(q="#loneliness", result_type="mixed",lang="en", count="100")
for tweet in public_tweets:
    print(tweet.created_at)
    # print(tweet.text)
    csvWriter.writerow([tweet.text.encode('utf-8')])