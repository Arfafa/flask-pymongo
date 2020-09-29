import os
from pymongo import MongoClient
from application.database.collection import Collection


class MongoConnection:
    _mongodb_uri = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/')
    _collection_solicitacao = None

    @classmethod
    def get_collection_solicitacao(cls):
        if cls._collection_solicitacao is None:

            client = MongoClient(cls._mongodb_uri)
            db = client['credito-cartao']

            cls._collection_solicitacao = Collection('solicitacao',
                                                     db['solicitacao'])

        return cls._collection_solicitacao
