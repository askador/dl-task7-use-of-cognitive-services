from pathlib import Path
import json
from detect_key_phrase import detect_sentiment

REVIEWS_PATH = Path(__file__).parent.joinpath('./reviews.json')

def update_reviews(hotel_id, review):

    with open(REVIEWS_PATH, 'r') as f:
        json_data = json.load(f)
        if not json_data.get(hotel_id):
            json_data[hotel_id] = []
        json_data[hotel_id].append(review)
        
    with open(REVIEWS_PATH, 'w') as f:
        f.write(json.dumps(json_data, indent=2, default=str))
    
    
def get_reviews(hotel_id):
    hotel_id = str(hotel_id)
    
    reviews = {
        'POSITIVE': [],
        'NEUTRAL': [],
        'MIXED': [],
        'NEGATIVE': []
    }
    
    with open(REVIEWS_PATH, 'r') as f:
        json_data = json.load(f)
        if not json_data.get(hotel_id):
            return {}
        
        for item in json_data[hotel_id]:
            text = item['text']
            reviews[detect_sentiment(text)].append(text)
        
    return reviews
        