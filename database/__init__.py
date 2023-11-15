from .db import Database
import app_config as config

# INITIALIZING THE DATABASE OBJECT
database = Database(config.CONST_DATABASE_NAME, config.CONST_MONGO_URL)

# CALL ON THE connect() METHOD IN ORDER TO ACTUALLY MAKE THE CONNECTION TO MongoDB
database.connect()