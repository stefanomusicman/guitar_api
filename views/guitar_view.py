from flask import Blueprint, request, jsonify
import json
from controllers.guitar_controller import create_guitar, fetch_guitars, search_by_brand, search_by_model, search_by_id

guitar = Blueprint("guitar", __name__)


# ADD A NEW GUITAR
@guitar.route("/v0/guitars/", methods=["POST"])
def create():
    try:
        # GET DATA BEING PASSED INTO THE REQUEST BODY
        data = json.loads(request.data)

        keys = ['year', 'brand', 'model', 'num_frets', 'ss_frets', 'wood', 'locking_tuners']

        # validate that all necessary fields have been provided in the request body
        for key in keys:
            if key not in data:
                return jsonify({'error': f'{key} must be provided in the request'}), 400
        
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
    try:
        return jsonify({'guitars': fetch_guitars()})

    except Exception:
        return jsonify({'error': 'Error when fetching all guitars.'}), 500
    
# SEARCH BY BRAND
@guitar.route("/v0/guitars/search-by-brand/<brand>", methods=["GET"])
def fetch_by_brand(brand):
    try:
        # No need to load request.data when using URL parameters
        return jsonify({'guitars': search_by_brand(brand)})

    except Exception as e:
        return jsonify({'error': f'Error when searching by brand: {str(e)}'}), 500
    
# SEARCH BY MODEL
@guitar.route("/v0/guitars/search-by-model/", methods=["GET"])
def fetch_by_model():
    try:
        data = json.loads(request.data)

        return jsonify({'guitars': search_by_model(data)})

    except Exception:
        return jsonify({'error': 'Error when searching by model'}), 500
    
# GET GUITAR BY ID
@guitar.route("/v0/guitars/<guitarUid>/", methods=["GET"])
def get_guitar_by_id(guitarUid):
    try:
        guitar = search_by_id(guitarUid)

        return guitar
    
    except Exception:
        return jsonify({'error': 'Something happened when getting the guitar'}), 500