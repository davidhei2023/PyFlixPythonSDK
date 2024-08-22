import requests


class Client:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.netflix.com/v1.0.2'

    def search_movies(self, query):
        endpoint = f'{self.base_url}/movies/search'
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        params = {
            'query': query
        }
        response = requests.get(endpoint, headers=headers, params=params)
        return response.json()

    def get_movie_details(self, movie_id):
        endpoint = f'{self.base_url}/movies/{movie_id}'
        headers = {
            'Authorization': f'Bearer {self.api_key}'
        }
        response = requests.get(endpoint, headers=headers)
        return response.json()
