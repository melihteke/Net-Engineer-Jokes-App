import tweepy
from dotenv import load_dotenv
import os
from ollama_prompt import ask_ollama
import time
import logging

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("app.log"),
                        logging.StreamHandler()
                    ])
logging.info("Access the environment variables are being loaded.")
# Access the environment variables
API_KEY = os.getenv('API_KEY')
API_KEY_SECRET = os.getenv('API_KEY_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')
BEARER_TOKEN = os.getenv('BEARER_TOKEN')


while True:
    try:
        logging.info("Requesting a Network Engineering joke.")
        prompt = ask_ollama(prompt_content="Tell me a Network Engineering Joke. Only return the joke, no other information. Use newline character to separate the joke from the answer and hashtags.")
        logging.info("Received joke: %s", prompt)

        logging.info("Requesting Network Engineering hashtags.")
        hashtags = ask_ollama(prompt_content="Write me a few Network Engineering hashtags. Maximum 5 hashtags. No other infomation only hashtag without index(count) numbering.")
        logging.info("Received hashtags: %s", hashtags)

        tweet = prompt + "\n \n" + hashtags
        logging.info("Composed tweet: %s", tweet)

        logging.info("Authenticating with Twitter API.")
        auth = tweepy.OAuth1UserHandler(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        
        api = tweepy.API(auth)
        logging.info("Authenticated with Twitter API using OAuth1.")

        client = tweepy.Client(bearer_token=BEARER_TOKEN, 
                                consumer_key=API_KEY, 
                                consumer_secret=API_KEY_SECRET, 
                                access_token=ACCESS_TOKEN, 
                                access_token_secret=ACCESS_TOKEN_SECRET)

        logging.info("Authenticated with Twitter API using Client.")
        
        logging.info("Sending Tweet.")
        # Send a tweet
        response = client.create_tweet(text=tweet)
        print("Tweet sent successfully")
    except Exception as e:
        logging.info("Error in sending Tweet.")
        print("Error sending tweet:", e)
        print("Tweet not sent")
        pass

    time.sleep( 30 * 60 ) # Sleep for 30 minutes
    logging.info("Another Iteration.")
