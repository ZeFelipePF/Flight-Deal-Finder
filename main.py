from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from pprint import pprint
import os
from datetime import datetime, timedelta
import time
from notification_manager import NotificationManager

os.system('cls')

ORIGIN_CITY_IATA = "LON"
data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_destinantion_data()
pprint(f'{sheet_data}')

for row in sheet_data:
    if row['iataCode'] == '':
        row['iataCode'] = flight_search.get_iata_code(row['city'])

data_manager.data = sheet_data
data_manager.update_destination_codes()       

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days = (6*30))

for destination in sheet_data:
    print(f'Getting flights for {destination['city']}...')
    flights = flight_search.check_flight(
        origin_city_code=ORIGIN_CITY_IATA,
        destination_city_code=destination['iataCode'],
        from_time=tomorrow,
        to_time=six_month_from_today,
    )
    cheapest_flight = find_cheapest_flight(flights)
    print(f"{destination['city']}: £{cheapest_flight.price}")
    time.sleep(2)

    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        print(f"Lower price flight found to {destination['city']}!")
        notification_manager.send_sms(
             message_body=f"Low price alert! Only £{cheapest_flight.price} to fly "
                          f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                          f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        )
        
        


