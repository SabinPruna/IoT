import sys
import time
import requests
from twython import Twython, TwythonError

#app keys to post on twitter @sabinpruna
apiKey = 'hHwsxqVTdiNYWxtxU9q122JgL'
apiSecret = 's6LPtfy1dnf00FaBujwqrXZohA7iK1DNyZzI5dnAHfbXqPnqKp'
accessToken = '2362223719-ITzqIFZCbGtuDzw9bcixmwzgDQncksAq5tO35re'
accessTokenSecret = '2djdlnA7fxEE1nIjkpcUorQotXxoCRnpZ3t2eSIMMNTty'

class TweeterBot:
    def __init__(self):
        #initialize api to send tweets on instance construction    
        self.api = Twython(apiKey, apiSecret, accessToken, accessTokenSecret)

    def send_tweet(self, data):
        try:
            tweet = data
            self.api.update_status(status = tweet)
            print("Tweeted:" + tweet)
        except TwythonError as error:
            print("Error:" + str(error))
       
        # start_time=time.time()
        # try:
        #     while True:
        #         tweetStr = 'tweet {counter}'.format(counter=self.counter)  
        #         counter = counter + 1
        #         api.update_status(status=tweetStr)        
        #         print("Tweeted: " + tweetStr)
        #         time.sleep(10)
        # except TwythonError as error:
        #     print(error) #in here you have to treat if the tweet is the same as the previous tweet which will result in an error