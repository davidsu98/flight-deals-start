API_KEY_TEQUILA = {'apikey':'Y8yt2oCEvp2YulBfBXIkOr3-34SPcY5J'}
tequila_url = 'https://api.tequila.kiwi.com/'
import datetime
import requests

class FlightData:

    #returns lowest price of flights between dates (1 year from tomorrow)
    def lowest_year(start, end):
        now = datetime.datetime.now()+datetime.timedelta(days=1)
        date1 = now.strftime('%d/%m/%Y')
        date2 = (now+datetime.timedelta(days=365)).strftime('%d/%m/%Y')

        flight_data_raw=requests.get(url = tequila_url+'search', params={'fly_from':start, 'fly_to':end, 'date_from':date1, 'date_to':date2, 'adults':1, 'curr':'CAD', 'vehicle_type':'aircraft'}, headers=API_KEY_TEQUILA)
        flight_data = flight_data_raw.json()['data']
        return flight_data[0]['price']
        #return the date of the cheapest flight


    #get data from google sheets on start and end cities. refills sheets with price?
    #do all at the same time. start end price?