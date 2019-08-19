from flask import Flask
from flask_restplus import Api, Resource
from flask import Flask, request
from flask_restplus import Api, Resource, fields
import json

flask_app = Flask(__name__)
app = Api(app = flask_app,
		  version = "1.0",
		  title = "API Estabelecimento",
		  description = "Desenvolvendo uma API Restfull com Flask")

# namespaces
estabelecimento = app.namespace('estabelecimento')
produtor = app.namespace('produtor')

# modelo
model = app.model('Estabelecimento Model',
				  {
						'nmEstabelecimento': fields.String(required = True, description="Nome do estabelecimento", help="Não pode ser em branco."),
						'nrCodigoOficial': fields.String(required = True, description="Código do estabelecimento", help="Não pode ser em branco."),
						'idPais': fields.Integer(required = True, description="Indice do país", help="Não pode ser em branco."),
						'idUf': fields.Integer(required = True, description="Indice do estado", help="Não pode ser em branco."),
						'idMunicipio': fields.Integer(required = True, description="Indice do município", help="Não pode ser em branco."),
						'nmLocalidade': fields.String(required = True, description="Nome da localidade", help="Não pode ser em branco."),
						'nrLatitude': fields.Integer(required = True, description="Latitude", help="Não pode ser em branco."),
						'nrLongitude': fields.Integer(required = True, description="Longitude", help="Não pode ser em branco."),
						'stAtivo': fields.Boolean(required = True, description="Status do cliente", help="Não pode ser em branco."),
						'idCliente': fields.Integer(required = True, description="Indice do cliente", help="Não pode ser em branco.")
					}
				)
model_produtor = app.model('Produtor Model',
				  {
						'nrDocumento': fields.String(required = True, description="Documento do produtor", help="Não pode ser em branco."),
						'nmProdutor': fields.String(required = True, description="Indice do país", help="Não pode ser em branco."),
						'nrTelefone': fields.String(required = True, description="Indice do estado", help="Não pode ser em branco."),
						'dsEmail': fields.String(required = True, description="Indice do município", help="Não pode ser em branco."),
						'cdEstabelecimento': fields.Integer(required = True, description="Nome da localidade", help="Não pode ser em branco."),
					}
				)

# Base de dados
estabelecimentos = [
	{
		'idEstabelecimento': 0,
		'nmEstabelecimento': 'Loja Feliz',
		'nrCodigoOficial': 'LojinhaFelizLTDA',
		'idPais': 55,
		'idUf': 1,
		'idMunicipio': 1,
		'nmLocalidade': 'Itajaí',
		'nrLatitude': 1,
		'nrLongitude': 2,
		'stAtivo': True,
		'idCliente': 0
	}
]

produtores = [{
	'idProdutor': 0,
	'nrDocumento': '456dd',
	'nmProdutor': 'João',
	'nrTelefone': '48999664100',
	'dsEmail': 'joao@gmail.com',
	'cdEstabelecimento': 0
}]

# ENDPOINTS ESTABELECIMENTO
@estabelecimento.route("/")
class EstabelecimentoMain(Resource):

	# get estabelecimentos
	@app.doc(responses={ 200: 'OK', 400: 'Argumentos Inválidos', 500: 'Erro interno' })
	def get(self):
		try:
			return {
				'status' : 'Lista de todos os estabelecimentos',
				'values' : estabelecimentos
			}
		except KeyError as e:
			estabelecimento.abort(500, e.__doc__, status = "Não é possível recuperar a informação", statusCode = "500")
		except Exception as e:
			estabelecimento.abort(400, e.__doc__, status = "Não é possível recuperar a informação", statusCode = "400")

	# post estabelecimento
	@app.doc(responses={ 200: 'OK', 400: 'Argumentos Inválidos', 500: 'Erro interno' })
	@app.expect(model)
	def post(self):
		try:
			estabelecimentos.append({
				'idEstabelecimento': len(estabelecimentos),
				'nmEstabelecimento': request.json['nmEstabelecimento'],
				'nrCodigoOficial': request.json['nrCodigoOficial'],
				'idPais': request.json['idPais'],
				'idUf': request.json['idUf'],
				'idMunicipio': request.json['idMunicipio'],
				'nmLocalidade': request.json['nmLocalidade'],
				'nrLatitude': request.json['nrLatitude'],
				'nrLongitude': request.json['nrLongitude'],
				'stAtivo': request.json['stAtivo'],
				'idCliente': request.json['idCliente']
			})

			return {
				"status": "Novo estabelecimento adicionado"
			}
		except KeyError as e:
			estabelecimento.abort(500, e.__doc__, status = "Não é possível salvar a informação", statusCode = "500")
		except Exception as e:
			estabelecimento.abort(400, e.__doc__, status = "Não é possível salvar a informação", statusCode = "400")

@estabelecimento.route("/<int:id>")
class EstabelecimentoId(Resource):

	@app.doc(responses={ 200: 'OK', 400: 'Argumentos Inválidos', 500: 'Erro interno' },
			 params={ 'id': 'Especifique o ID do estabelecimento' })
	def get(self, id):
		try:
			return {
				"status": "Estabelecimento consultado",
				"name" : estabelecimentos[id]
			}
		except KeyError as e:
			estabelecimento.abort(500, e.__doc__, status = "Não é possível recuperar a informação", statusCode = "500")
		except Exception as e:
			estabelecimento.abort(400, e.__doc__, status = "Não é possível recuperar a informação", statusCode = "400")

	@app.doc(responses={ 200: 'OK', 400: 'Argumentos Inválidos', 500: 'Erro interno' },
			 params={ 'id': 'Especifique o ID do estabelecimento' })
	@app.expect(model)
	def put(self, id):
		try:
			estabelecimentos[id] = {
				'idEstabelecimento': estabelecimentos[id]['idEstabelecimento'],
				'nmEstabelecimento': request.json['nmEstabelecimento'],
				'nrCodigoOficial': request.json['nrCodigoOficial'],
				'idPais': request.json['idPais'],
				'idUf': request.json['idUf'],
				'idMunicipio': request.json['idMunicipio'],
				'nmLocalidade': request.json['nmLocalidade'],
				'nrLatitude': request.json['nrLatitude'],
				'nrLongitude': request.json['nrLongitude'],
				'stAtivo': request.json['stAtivo'],
				'idCliente': request.json['idCliente']
			}
			return {
				"status": "Estabelecimento atualizado",
				"name": estabelecimentos[id]
			}
		except KeyError as e:
			estabelecimento.abort(500, e.__doc__, status = "Não é possível salvar a informação", statusCode = "500")
		except Exception as e:
			estabelecimento.abort(400, e.__doc__, status = "Não é possível salvar a informação", statusCode = "400")


# ENDPOINTS PRODUTORES
@produtor.route("/")
class ProdutorMain(Resource):
	# get produtores
	@app.doc(responses={ 200: 'OK', 400: 'Argumentos Inválidos', 500: 'Erro interno' })
	def get(self):
		try:
			return {
				'status' : 'Lista de todos os produtores',
				'values' : produtores
			}
		except KeyError as e:
			produtor.abort(500, e.__doc__, status = "Não é possível recuperar a informação", statusCode = "500")
		except Exception as e:
			produtor.abort(400, e.__doc__, status = "Não é possível recuperar a informação", statusCode = "400")

	# post produtores
	@app.doc(responses={ 200: 'OK', 400: 'Argumentos Inválidos', 500: 'Erro interno' })
	@app.expect(model_produtor)
	def post(self):
		try:
			produtores.append({
				'idProdutor': len(produtores),
				'nrDocumento': request.json['nrDocumento'],
				'nmProdutor': request.json['nmProdutor'],
				'nrTelefone': request.json['nrTelefone'],
				'dsEmail': request.json['dsEmail'],
				'cdEstabelecimento': request.json['cdEstabelecimento'],
			})
			return {
				"status": "Novo produtor adicionado"
			}
		except KeyError as e:
			estabelecimento.abort(500, e.__doc__, status = "Não é possível salvar a informação", statusCode = "500")
		except Exception as e:
			estabelecimento.abort(400, e.__doc__, status = "Não é possível salvar a informação", statusCode = "400")

@produtor.route("/<int:id>")
class ProdutorId(Resource):
	@app.doc(responses={ 200: 'OK', 400: 'Argumentos Inválidos', 500: 'Erro interno' },
			 params={ 'id': 'Especifique o ID do produtor' })
	def get(self, id):
		try:
			return {
				'status' : 'Produtor',
				'values' : produtores[id]
			}
		except KeyError as e:
			produtor.abort(500, e.__doc__, status = "Não é possível recuperar a informação", statusCode = "500")
		except Exception as e:
			produtor.abort(400, e.__doc__, status = "Não é possível recuperar a informação", statusCode = "400")

	@app.doc(responses={ 200: 'OK', 400: 'Argumentos Inválidos', 500: 'Erro interno' },
			 params={ 'id': 'Especifique o ID do Produtor' })
	@app.expect(model_produtor)

	def put(self, id):
		try:

			produtores[id] = {
				'idProdutor': produtores[id]['idProdutor'],
				'nrDocumento': request.json['nrDocumento'],
				'nmProdutor': request.json['nmProdutor'],
				'nrTelefone': request.json['nrTelefone'],
				'dsEmail': request.json['dsEmail'],
				'cdEstabelecimento': request.json['cdEstabelecimento'],
			}
			return {
				"status": "Produtor atualizado"
			}
		except KeyError as e:
			estabelecimento.abort(500, e.__doc__, status = "Não é possível salvar a informação", statusCode = "500")
		except Exception as e:
			estabelecimento.abort(400, e.__doc__, status = "Não é possível salvar a informação", statusCode = "400")
