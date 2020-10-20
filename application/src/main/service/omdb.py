from main.repository.dlake import Dlake
from main.app import logger
import aiohttp
import asyncio
import requests
import json

from main.repository.dlake import Dlake
from main.repository.collection import Collection

class OMDB():

    def get_request2(self,source_uri, headers):
        try:
            res = requests.get(source_uri,headers=headers)
            return {'html': res.text, 'status': res.status_code, 'url': res.url, 'original_url': source_uri}
        except requests.RequestException:
            return

    def _get_search_result(self, query):
        endpoint = 'http://www.omdbapi.com/?s='+query+'&apikey=5f89d448'
        headers = {}
        response = self.get_request2(endpoint,headers)
        return json.loads(response['html'])

    def search(self, query):
        result = self._get_search_result(query=query)
        output = {
            'results':[],
            'total':result['totalResults'],
            'response':result['Response']
        }
        for i in result['Search']:
            item = Dlake().create(imdb=i['imdbID'],data=i)
            cllc = Collection().create(data={"imdb":i['imdbID'],"genre":"action","description":"A saga de um verdadeiro herói"})
            output['results'].append({
                "title": i['Title'],
                "year": i['Year'],
                "imdb_id": i['imdbID'],
                "type": i['Type'],
                "poster": i['Poster'],
                "meta": {}
            })
        return output
