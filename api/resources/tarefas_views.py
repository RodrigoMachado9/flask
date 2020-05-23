from flask_restful import Resource


class TarefaList(Resource):
    def get(self):
        return {
            "status": "succes",
            "message": ""
        }


    def post(self):
        return {
            "status": "success",
            "message": ""
        }
