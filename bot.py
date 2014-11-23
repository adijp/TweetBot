import tweepy, time, sys


#Tweets every single line from filenameofyourchoice
#The below required access codes can be created at dev.twitter.com using a Twitter account


#Required tweepy
#On the command line, enter pip install tweepy
#If it required authorisation, then enter pip install tweepy --user
#Else https://github.com/tweepy/tweepy and follow the instructions


argfile = str(sys.argv[1])

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = ''#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = ''#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = ''#keep the quotes, replace this with your access token
ACCESS_SECRET = ''#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open(argfile,'r')
lines=filename.readlines()
filename.close()

for i in lines:
    api.update_status(i)
    #It can also be modified to be api.update_status("Hello world " + i)
    #or ("@twitter-name " + i) if tweeting to a particular user
    print "Tweeted", i

# input -> python bot.py filenameofyourchoice

#Note: filenameofyourchoice must exist in the same directory as bot.py
