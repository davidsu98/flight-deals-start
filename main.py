#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_data import FlightData
import datetime

# start_city = input('Which city would you like to fly from?: ')
# date = input('Please input date (dd/mm/yyyy): ')

# top_des_city = DataManager.starting_loc(start_city)

# DataManager.fill_sheet(top_des_city, start_city, date)

print(FlightData.lowest_year('YVR', 'YYZ'))