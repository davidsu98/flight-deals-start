#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_data import FlightData
import datetime

start_city = input('Which city would you like to fly from?: ')
date = input('Please input date (dd/mm/yyyy): ')

top_des_city = DataManager.starting_loc(start_city)

DataManager.fill_sheet(top_des_city, start_city, date)
select_city = input(f'Please select a city from the following list:\n{[(top_des_city[i]["name"],top_des_city[i]["code"]) for i in range(len(top_des_city))]}\n')


print(FlightData.lowest_year(start_city, select_city))