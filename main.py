#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager


start_city = input('Which city would you like to fly from?: ')

original_city = DataManager.starting_loc(start_city)

DataManager.fill_iata(original_city)
