from pymongo import MongoClient

class Database():
    # CONSTRUCTOR
    def __init__(self, databaseName = None, connectionString = None):
        if databaseName == None or connectionString == None:
            raise Exception("MongoDB requires a Database Name and String Connection!")
        
        self.__databaseName = databaseName
        self.__connectionString = connectionString
        self.__dbConnection = None
        self.__dataBase = None

    @property
    def dataBase(self):
        return self.__dataBase
    
    @property
    def dbConnection(self):
        return self.__dbConnection
    
    # RESPONSIBLE FOR MAKING THE CONNECTION TO THE DATABASE
    def connect(self):
        try:
            self.__dbConnection = MongoClient(self.__connectionString)
            dbName = str(self.__databaseName)
            self.__dataBase = self.__dbConnection[dbName]
            return True

        except Exception as err:
            print("Mongo connection error", err)
            return False