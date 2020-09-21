from flask import request
from flask_restful import Resource
from application.server import api
from application.database.utils import get_collection_solicitacao
from application.routes.utils import get_json, get_from_request
from application.routes.utils import HTTP_STATUS_CODE
from application.routes.logs import error_log


class Solicitacao(Resource):
    def get(self):
        sol = get_collection_solicitacao()

        return sol.listar_solicitacoes(), HTTP_STATUS_CODE['OK']

    def post(self):
        try:
            data = get_json(request)

            sol = get_collection_solicitacao()

            document = sol.inserir_solicitacao(data)

        except Exception as e:
            resp = {'msg': str(e)}

            error_log('/solicitacao', 'POST', str(e))

            return resp, HTTP_STATUS_CODE['BAD_REQUEST']

        return document, HTTP_STATUS_CODE['OK']

    def delete(self):
        try:
            data = get_json(request)
            sol_id = get_from_request(data, 'id')

            sol = get_collection_solicitacao()

            resp = sol.deletar_solicitacao(sol_id)

        except Exception as e:
            resp = {'msg': str(e)}

            error_log('/solicitacao', 'DELETE', str(e))

            return resp, HTTP_STATUS_CODE['BAD_REQUEST']

        return resp, HTTP_STATUS_CODE['OK']


def init_routes():
    api.add_resource(Solicitacao, '/solicitacao')
