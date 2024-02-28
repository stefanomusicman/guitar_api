import os
from datetime import datetime

try:
    import secret
except:
    pass

# Collection desta API
CONST_MONGO_URL = os.environ.get("CONST_MONGO_URL")
CONST_DATABASE_NAME = os.environ.get("CONST_DATABASE_NAME")

CONST_GUITAR_COLLECTION = os.environ.get("CONST_GUITAR_COLLECTION")
CONST_USER_COLLECTION = os.environ.get("CONST_USER_COLLECTION")


