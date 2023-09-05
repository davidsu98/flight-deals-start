API_KEY_TEQUILA = {'apikey':'Y8yt2oCEvp2YulBfBXIkOr3-34SPcY5J'}
tequila_url = 'https://api.tequila.kiwi.com/'
import datetime
import requests

class FlightData:
    def search(start, end, date=str):
        flight_data_raw=requests.get(url = tequila_url+'search', params={'fly_from':start, 'fly_to':end, 'date_from':date, 'date_to':date, 'adults':1, 'curr':'CAD', 'vehicle_type':'aircraft'}, headers=API_KEY_TEQUILA)
        flight_data = flight_data_raw.json()['data']
        print(str(flight_data[0]['price']) + ' you r so poor to fly with: ' + flight_data[0]['airlines'][0])


    #get data from google sheets on start and end cities. refills sheets with price?
    #do all at the same time. start end price?