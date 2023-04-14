import boto3
from environ import Env

env = Env()
env.read_env()

client = boto3.client(
    service_name='comprehend',
    aws_access_key_id=env.str('AWS_ACCESS_KEY'),
    aws_secret_access_key=env.str('AWS_SECRET_ACCESS_KEY'),
    region_name='us-east-1'
)

def detect_sentiment(text):
    sentiment = client.detect_sentiment(Text=text, LanguageCode='en')
    return sentiment['Sentiment']

def detect_key_phrase(text):
    key_phrases = client.detect_key_phrases(Text=text, LanguageCode='en')
    response = list(set([item['Text'] for item in key_phrases['KeyPhrases']]))
    return response