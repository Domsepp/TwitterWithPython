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
    for tweet in tweepy.Cursor(api.search,q='@DonaldTrump',lang='en').items(10):
        try:
            #print ("Found tweet by: @"+tweet.user.screen_name)

            #tweet.retweet()
            #print tweet
            print tweet.text
            #tweet.favourite()
            print "favourited"
        except tweepy.TweepError as e:
            print e.reason
            time.sleep(0.1)
            continue
        except StopIteration:
            break

#gettweets()

user = api.get_user(screen_name = '@Domsepp')
print user.name
print user


