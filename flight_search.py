import os
from dotenv import load_dotenv
import requests

load_dotenv()

class FlightSearch:
    def __init__(self):
        self._api_key = os.environ['AMADEUS_API_KEY']
        self._amadeus_api_secret = os.environ['AMADEUS_API_SECRET']
        self._token = self._get_new_token()

    def get_iata_code(self, city_name):
        headers = {
            "Authorization": f"Bearer {self._token}"
        }
        
        query_params = {
            'keyword': city_name,
            'max': '2',
            'include' : 'AIRPORTS'
        }

        url = 'https://test.api.amadeus.com/v1/reference-data/locations/cities'

        try:
            response = requests.get(url=url, headers=headers, params=query_params)
            response.raise_for_status()
            return response.json()['data'][0]['iataCode']
        except (KeyError, IndexError):
            print(f'Nenhum resultado encontrado na API para {city_name}')
            return 'N/A'
        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição para {city_name}: {e}")
            return 'N/A'
    
    def _get_new_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._amadeus_api_secret,
        }

        url = 'https://test.api.amadeus.com/v1/security/oauth2/token'

        try:
            response = requests.post(url=url, headers=header, data=body)
            response.raise_for_status()
            
            return response.json()['access_token']

        except requests.exceptions.RequestException as error:
            print(f"Erro ao obter token: {error}")
            return None
        
    def check_flight(self, origin_city_code, destination_city_code, from_time, to_time):

        headers = {
            "Authorization": f"Bearer {self._token}"
        }
        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "GBP",
            "max": "10",
        }

        response = requests.get(
            url = 'https://test.api.amadeus.com/v2/shopping/flight-offers',
            headers=headers,
            params=query,
        )

        if response.status_code != 200:
            print(f'check_flights() response code: {response.status_code}')
            print('Response body:', response.text)
            return None
        
        return response.json()