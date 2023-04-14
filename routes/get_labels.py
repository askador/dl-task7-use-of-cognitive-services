from utils import get_reviews
from detect_key_phrase import detect_key_phrase
from app import app
from flask import jsonify


@app.route('/getLabels/<hotel_id>', methods=['GET'])
def get_labels(hotel_id):
    classified_reviews = get_reviews(hotel_id)
    
    res = {
        'POSITIVE': [],
        'NEGATIVE': []
    }
    
    for sentiment in ['POSITIVE', 'NEGATIVE']:
        key_phrases = detect_key_phrase('. '.join(classified_reviews[sentiment]))
        res[sentiment] += key_phrases

    res = {key: sorted(list(set(labels))) for key, labels in res.items()}

    return jsonify(res)


