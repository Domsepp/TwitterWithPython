import tweepy
import time
fortweettext = ''

consumer_key = 'Consumer Key'
consumer_secret = 'Consumer Secret'
access_token = 'Access Token'
access_token_secret = 'Access Token Secret'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
auth.secure = True
api = tweepy.API(auth)

def gettweets():
    for tweet in tweepy.Cursor(api.search,q='search text or hashtag',lang='en').items(10):
        try:
            #print ("Found tweet by: @"+tweet.user.screen_name)                         # print the user name tweeted this tweet

            #tweet.retweet()                                                            # retweet the current tweet
            #print tweet                                                                # print all data stored in 'tweet'
            print tweet.text
            #tweet.favourite()                                                          # favourite the current tweet
            print "favourited"
        except tweepy.TweepError as e:                                                  # error handling
            print e.reason
            time.sleep(0.1)
            continue
        except StopIteration:
            break

gettweets()

user = api.get_user(screen_name = '@Domsepp')                                           # get data from user and store it in the "user" variable
print user.name
print user


