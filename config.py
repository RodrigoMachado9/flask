DEBUG = True

# instrumentation api!
from flask import Flask
from flask_restful import Api
from api.resources.tarefas_views import TarefaList

app = Flask(__name__)
app.config.from_object('config')
# param-rest
api = Api(app)

api.add_resource(TarefaList, '/go')