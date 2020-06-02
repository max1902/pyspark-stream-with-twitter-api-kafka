import json

from kafka import KafkaProducer
from tweepy import Stream
from tweepy.auth import OAuthHandler
from tweepy.streaming import StreamListener

ACCESS_TOKEN = ''
ACCESS_SECRET_TOKEN = ''
API_KEY = ''
API_SECRET_KEY = ''


class TweetsListener(StreamListener):

    def __init__(self):
        self.count = 0
        self.kafka_producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

    def on_connect(self):
        print('Connected with success...')

    def on_data(self, data):
        try:
            tweet_obj = json.loads(data)
            msg = json.dumps({
                'user_name': tweet_obj['user']['screen_name'],
                'user_tweet': tweet_obj['text'],
                'followers': tweet_obj['user']['followers_count'],
                'friends': tweet_obj['user']['friends_count'],
            })
            self.kafka_producer.send('tweets', msg.encode('utf-8'))
            print(msg)
            return True

        except BaseException as exp:
            return False

    def on_error(self, status_code):
        print(f'Status code is: {status_code}')
        return False


if __name__ == '__main__':
    auth = OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET_TOKEN)
    twitter_stream = Stream(auth, TweetsListener())
    twitter_stream.filter(languages=['en'], track=['football'])
