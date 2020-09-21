import random
from bson.objectid import ObjectId


class Collection:
    def __init__(self, name, collection):
        self.name = name
        self.collection = collection

    def __str__(self):
        return self.name

    def listar_solicitacoes(self):
        documents = []

        for doc in self.collection.find():
            doc['id'] = str(doc.pop('_id'))

            documents.append(doc)

        return documents

    def inserir_solicitacao(self, document):
        credito = self._verificar_credito(document['renda'])

        document['credito'] = credito

        self.collection.insert_one(document)

        document = self.collection.find_one(document)
        document['id'] = str(document.pop('_id'))

        return document

    def deletar_solicitacao(self, document_id):
        _id = ObjectId(document_id)

        document = self.collection.find_one({'_id': _id})

        if document:
            self.collection.delete_one({'_id': _id})
            document['id'] = str(document.pop('_id'))

        else:
            msg = 'Solicitacao com o id: ' + document_id
            msg += ' nao encontrada'

            document = {'msg': msg}

        return document

    def _verificar_credito(self, renda):
        aux = random.randint(1, 999)

        if aux < 300:
            credito = 0

        elif aux < 600:
            credito = 1000

        elif aux < 800:
            credito = max(1000, renda/2)

        elif aux < 951:
            credito = 2*renda

        else:
            credito = 1000000

        return credito
