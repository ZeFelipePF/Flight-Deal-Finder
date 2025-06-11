from dotenv import load_dotenv
import os
import requests

load_dotenv()

SHEETY_PRICES_ENDPOINT = os.environ['SHEETY_API']

class DataManager():
    def __init__(self):
        self.sheet_url = SHEETY_PRICES_ENDPOINT
        self.data = []
        
    def get_destinantion_data(self):
        response = requests.get(self.sheet_url)
        response.raise_for_status()
        data = response.json()
        self.data = data['prices']
        return self.data
    
    def update_destination_codes(self):
        for city in self.data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{self.sheet_url}/{city['id']}",
                json=new_data,
            )
            print(response.text)