import os
from pymongo import MongoClient
from application.database.collection import Collection

mongodb_uri = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/')
client = MongoClient(mongodb_uri)
db = client['credito-cartao']

SOLICITACAO = Collection('solicitacao', db['solicitacao'])


def get_collection_solicitacao():
    return SOLICITACAO
