from flask import Blueprint, request, jsonify
import json
from controllers.guitar_controller import create_guitar

guitar = Blueprint("guitar", __name__)


# ADD A NEW GUITAR
@guitar.route("/v0/guitars/", methods=["POST"])
def create():
    try:
        # GET DATA BEING PASSED INTO THE REQUEST BODY
        data = json.loads(request.data)
        print(data)

        # validate that all necessary fields have been provided in the request body
        if 'year' not in data:
            return jsonify({'error': 'Year must be provided in the request.'}), 400
        
        if 'brand' not in data:
            return jsonify({'error': 'Brand must be provided in the request.'}), 400
        
        if 'model' not in data:
            return jsonify({'error': 'Model must be provided in the request.'}), 400
        
        if 'num_frets' not in data:
            return jsonify({'error': 'Number of frets must be provided in the request.'}), 400
        
        if 'ss_frets' not in data:
            return jsonify({'error': 'Stainless Steel frets must be provided in the request.'}), 400
        
        if 'wood' not in data:
            return jsonify({'error': 'Wood must be provided in the request.'}), 400
        
        if 'locking_tuners' not in data:
            return jsonify({'error': 'Locking Tuners must be provided in the request.'}), 400
        
        created_guitar = create_guitar(data)

        if created_guitar == "Duplicate Guitar":
            return jsonify({'error': 'Guitar with this brand, year and model already exists.'}), 400
        
        if not created_guitar.inserted_id:
            return jsonify({'error': 'Something went wrong when creating the guitar'}), 500
        
        return jsonify({'id': str(created_guitar.inserted_id)})
    
    except:
        return jsonify({'error': 'Something went wrong when creating a new guitar.'}), 500




# GET ALL GUITARS
@guitar.route("/v0/guitars/", methods=["GET"])
def fetchAll():
    pass