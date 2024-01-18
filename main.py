#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_data import FlightData
import datetime

start_city = input('Which city would you like to fly from? (IATA): ')



top_des_city = DataManager.starting_loc(start_city)

#   the following function fills an excel sheet using sheety [top destination, iata, price]
#   DataManager.fill_sheet(top_des_city, start_city, date)

#destination selection
city_select = input('Please enter your preferred Destination (IATA) or if you want to choose from Suggested Destinations, type "continue":\n')

if city_select == 'continue':
    select_city = input(f'Select a Top 10 Destinations from {start_city}:\n{[(top_des_city[i]["name"],top_des_city[i]["code"]) for i in range(len(top_des_city))]}\nOr if destination not listed input your own (IATA):\n')
else:
    select_city = city_select
#date selection
date = input('Please input date (dd/mm/yyyy) or "continue" to see cheapest options:\n')

if date == 'continue':
    print(f'Displaying cheapest dates to fly in the upcoming 365 days:\n{FlightData.lowest_year(start_city, select_city)}')
else:
    print('this function not ready')

#make the selection able to backtrack, "reselect", "back", "cancel", etc