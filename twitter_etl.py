import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs


def run_twitter_etl():

    bearer_token = "BEARERTOKEN_KEY"
    client = tweepy.Client(bearer_token=bearer_token, wait_on_rate_limit=True)

    # Auth twitter
    auth = tweepy.OAuth2BearerHandler('bearer_token')

    # Objeto para API
    api = tweepy.API(auth)


    # Usuário em que vai ser usado para pesquisa
    name = 'elonmusk'

    # Busca pelo user data
    user = client.get_user(username = name).data

    # Extrair o id e o nome do usuário
    user_id = user.id
    user_name = user.name

    # Busca pelos tweets do usuário
    tweets = client.get_users_tweets(id = user_id, tweet_fields = ['created_at', 'geo', 'public_metrics'])


    tweet_list = []

    for tweet in tweets.data:

        refined_tweet = {"user": user.name,
                         "text": tweet,
                         "favorite_count": tweet.public_metrics['like_count'],
                         "retweet_count": tweet.public_metrics['retweet_count'],
                         "created_at": tweet.created_at
                         }
        tweet_list.append(refined_tweet)



    df = pd.DataFrame(tweet_list)
    df.to_csv("s3://bucketvictorgomes/elonmusk_twitter_data.csv")

