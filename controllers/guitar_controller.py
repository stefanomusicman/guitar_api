from models.guitar_model import Guitar
from database.__init__ import database
import app_config as config
from bson.objectid import ObjectId
from flask import jsonify
import re

def create_guitar(guitar_information):
    try:
        new_guitar = Guitar()
        new_guitar.year = int(guitar_information['year'])
        new_guitar.brand = guitar_information['brand']
        new_guitar.model = guitar_information['model']
        new_guitar.num_frets = int(guitar_information['num_frets'])
        new_guitar.ss_frets = bool(guitar_information['ss_frets'])
        new_guitar.wood = guitar_information['wood']
        new_guitar.locking_tuners = bool(guitar_information['locking_tuners'])

        collection = database.dataBase[config.CONST_GUITAR_COLLECTION]

        # check to see if theres already a guitar with the same brand, model and year
        if collection.find_one({'year': int(new_guitar.year), 'brand': new_guitar.brand, 'model': new_guitar.model}):
            return "Duplicate Guitar"
        
        created_guitar = collection.insert_one(new_guitar.__dict__)

        return created_guitar
    
    except Exception as err:
        print("Error when attempting to create a new guitar.", err)    

def fetch_guitars():
    try:
        collection = database.dataBase[config.CONST_GUITAR_COLLECTION]

        guitars = []

        for guitar in collection.find():
            current_guitar = {}
            current_guitar['uid'] = str(guitar['_id'])
            current_guitar['year'] = guitar['year']
            current_guitar['brand'] = guitar['brand']
            current_guitar['model'] = guitar['model']
            current_guitar['num_frets'] = guitar['num_frets']
            current_guitar['ss_frets'] = guitar['ss_frets']
            current_guitar['wood'] = guitar['wood']
            current_guitar['locking_tuners'] = guitar['locking_tuners']
            guitars.append(current_guitar)

        return guitars    

    except Exception as err:
        print("Error when fetching the guitars.", err)

def search_by_brand(brand):
    try:
        collection = database.dataBase[config.CONST_GUITAR_COLLECTION]

        regex = re.compile(brand, re.IGNORECASE)

        guitars = []

        for guitar in collection.find({'brand': {'$regex': regex}}):
            current_guitar = {}
            current_guitar['uid'] = str(guitar['_id'])
            current_guitar['year'] = guitar['year']
            current_guitar['brand'] = guitar['brand']
            current_guitar['model'] = guitar['model']
            current_guitar['num_frets'] = guitar['num_frets']
            current_guitar['ss_frets'] = guitar['ss_frets']
            current_guitar['wood'] = guitar['wood']
            current_guitar['locking_tuners'] = guitar['locking_tuners']
            guitars.append(current_guitar)

        return guitars  

    except Exception as err:
        print("Error when attempting to search for guitars.", err)

def search_by_model(model):
    try:
        collection = database.dataBase[config.CONST_GUITAR_COLLECTION]

        regex = f'.*{model}.*'

        guitars = []

        for guitar in collection.find({'model': {'$regex': regex, '$options': 'i'}}):
            current_guitar = {}
            current_guitar['uid'] = str(guitar['_id'])
            current_guitar['year'] = guitar['year']
            current_guitar['brand'] = guitar['brand']
            current_guitar['model'] = guitar['model']
            current_guitar['num_frets'] = guitar['num_frets']
            current_guitar['ss_frets'] = guitar['ss_frets']
            current_guitar['wood'] = guitar['wood']
            current_guitar['locking_tuners'] = guitar['locking_tuners']
            guitars.append(current_guitar)

        return guitars

    except Exception as err:
        print("Error when attempting to search for guitars.", err)

def search_by_id(guitarId):
    try:
        guitar_id = ObjectId(guitarId)

        collection = database.dataBase[config.CONST_GUITAR_COLLECTION]

        result = collection.find_one({'_id': guitar_id})

        if result:
            result['_id'] = str(result['_id'])
            return jsonify(result)
        else:
            return jsonify({'error': 'Guitar not found'}), 400
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400