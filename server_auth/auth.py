import pymongo
from urllib.parse import quote_plus
from utils import app_strings

class Auth:
    client = None
    def __init__(self) -> None:
        username = quote_plus('omkarraut2355')
        password = quote_plus('Omkar@123')
        Auth.client = pymongo.MongoClient(app_strings.database_connection_link % (username, password))

    @staticmethod
    def db_for_application():
        if Auth.client:
            return Auth.client.NoteApplicationDB
        return app_strings.database_connection_fail