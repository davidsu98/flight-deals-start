import requests

sheety_url = 'https://api.sheety.co/b986aa330f6b7bd3394167dfe6964521/flightDeals/prices'
# .put() sheety_url + [object id]..
# object id = row number
tequila_url = 'https://api.tequila.kiwi.com/'
top_des_url = tequila_url+'locations/topdestinations'
loc_query_url = tequila_url+'locations/query'
API_KEY_TEQUILA = {'apikey':'Y8yt2oCEvp2YulBfBXIkOr3-34SPcY5J'}

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    #starting location user input: can be name of city or airport
    #inputs top 10 destination names and IATA (Tequila) into google sheet (Sheety)

    #returns top 10 des from city json
    def starting_loc(user_city):
        city_id = requests.get(url = loc_query_url, params = {'term':user_city}, headers=API_KEY_TEQUILA)
        city_id_data = city_id.json()['locations']
        top_des = requests.get(url= top_des_url , params = {'term':city_id_data[0]['id'], 'limit':10}, headers = API_KEY_TEQUILA)
        top_des_data = top_des.json()['locations']
        return top_des_data



    #fills google sheets with top 10 destinations and lowest price
    def fill_sheet(top_des_data, ori_city, date=str):

        for i in range(len(top_des_data)):
            cur_city = top_des_data[i]['name']
            cur_IATA = top_des_data[i]['code']

            flight_data_raw=requests.get(url = tequila_url+'search', params={'fly_from':ori_city, 'fly_to':cur_IATA, 'date_from':date, 'date_to':date, 'adults':1, 'curr':'CAD', 'vehicle_type':'aircraft'}, headers=API_KEY_TEQUILA)
            flight_data = flight_data_raw.json()['data']

            requests.put(url = sheety_url+f'/{i+2}', json = {'price':{'city':cur_city, 'iataCode':cur_IATA, 'lowestPrice':flight_data[0]['price']}})

    
    #filling price and date of trips

    
        # response = requests.get(url=sheety_url)

        # #LIST of dictionaries for data in google sheets
        # data_list = response.json()['prices']
        # print(data_list)
        # adding IATA through sheety through Tequila api
        # for i in range(len(data_list)):
        #     cur_city = data_list[i]['city']
        #     id = requests.get(url = loc_query_url, params = {'term':cur_city}, headers=API_KEY_TEQUILA)
        #     IATA = id.json()['locations'][0]['code']
        #     requests.put(url = sheety_url+f'/{i+2}', json = {'price':{'iataCode':IATA}})

