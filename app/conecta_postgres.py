import psycopg2
import time
from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app, version='1.0', title='Atividade 3',
          description='Atividade 3',
          doc='/swagger')

ns = api.namespace('Soma', description='post com a soma de 2 valores numéricos')

@ns.route('/')
class soma(Resource):
    def postsoma(varx, vary):
        svolta = str("soma: " + (varx + vary))
        return svolta

ms = api.namespace('Mult', description='post com a multiplicação de 2 valores numéricos')

@ms.route('/mult')
class mult(Resource):
    def postmult(vara, varb):
        mvolta = str("Multiplicação: " + (vara + varb))
        return mvolta

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
