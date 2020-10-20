from flask_restful import Resource, fields, marshal_with, request
from main.service.omdb import OMDB
from main.model.dlake import Dlake
from main.repository.collection import Collection
from flask_restful import reqparse


class Search(Resource):
    """
    Management of available currencies
    """

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('query', type=str, required=True, help='Inform query')
        parser.add_argument('Authorization', required=True, location='headers')
        args = parser.parse_args()

        '''
        TODO: Validação do header 'Authorization'... (Não será implementada por falta de tempo)
        Mas haveria um modulo para isso, que consumiria de um repositório (local ou não), e faria as validações
        '''

        data = OMDB().search(query=args['query'])

        if data:
            output = {
                'results':[],
                'total':0
                ,'args':args
            }

            if data and len(data['results']) > 0:
                eanhanced_results = []


                for i in data['results']:
                    collection = Collection().find(query={'imdb':i['imdb_id']})
                    if len(collection) > 0:
                        desc = collection[0]['description']
                        genre = collection[0]['genre']
                    else:
                        desc = None
                        genre = None
                    i['meta'] = {
                        'genre':genre,
                        'description':desc
                    }
                    eanhanced_results.append(i)

                output['results'] = eanhanced_results
                output['total'] = data['total']

            return output, 200
        else:
            raise Exception('Movie not found', 404)
