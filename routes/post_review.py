from flask import request, jsonify
from app import app
from datetime import datetime
from utils import update_reviews

@app.route('/review', methods=["POST"])
def upload_review():
    data = request.get_json()
    if not all(key in data for key in ['review', 'hotelId']):
        return jsonify({'errorMessage': 'Your request must contain "review" and "hotelId" values'}), 400
    
    review_text = data['review']
    hotel_id = data['hotelId']
    
    review = {
        "date": datetime.now().isoformat(),
        "audioId": None,
        "text": review_text
    }
    
    update_reviews(hotel_id, review)
    
    return 'Ok'