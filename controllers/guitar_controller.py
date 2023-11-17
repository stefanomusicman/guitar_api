from models.guitar_model import Guitar
from database.__init__ import database
import app_config as config
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

def search_by_brand(body_data):
    try:
        collection = database.dataBase[config.CONST_GUITAR_COLLECTION]

        search_term = body_data['brand']
        regex = re.compile(search_term, re.IGNORECASE)

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

def search_by_model(body_data):
    try:
        collection = database.dataBase[config.CONST_GUITAR_COLLECTION]

        search_term = body_data['model']
        regex = f'.*{search_term}.*'

        guitars = []

        for guitar in collection.find({'model': {'$regex' : regex, '$options': 'i'}}):
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