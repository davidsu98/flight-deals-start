API_KEY_TEQUILA = {'apikey':'Y8yt2oCEvp2YulBfBXIkOr3-34SPcY5J'}
tequila_url = 'https://api.tequila.kiwi.com/'
from datetime import datetime
from datetime import timedelta
import requests

class FlightData:

    #returns {lowest price:date} of flights between (1 year from tomorrow)
    def lowest_year(start, end):
        now = datetime.now()+ timedelta(days=1)
        date1 = now.strftime('%d/%m/%Y')
        date2 = (now+timedelta(days=365)).strftime('%d/%m/%Y')

        flight_data_raw=requests.get(url = tequila_url+'search', params={'fly_from':start, 'fly_to':end, 'date_from':date1, 'date_to':date2, 'adults':1, 'curr':'CAD', 'vehicle_type':'aircraft', 'limit':10, 'max_stopovers':0}, headers=API_KEY_TEQUILA)
        flight_data = flight_data_raw.json()['data']

        return [(flight_data[i]['price'],datetime.fromtimestamp(flight_data[i]['dTime']).strftime('%Y-%m-%d')) for i in range(len(flight_data))] 

    #get data from google sheets on start and end cities. refills sheets with price?
    #do all at the same time. start end price?
