from flask_restful import Resource


class TarefaList(Resource):
    def get(self):
        return {
            "status": "succes",
            "message": "hello-world get"
        }


    def post(self):
        return {
            "status": "success",
            "message": "posted is ok"
        }
