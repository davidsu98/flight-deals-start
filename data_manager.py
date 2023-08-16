import requests
class DataManager:
    #This class is responsible for talking to the Google Sheet.


    sheety_url = 'https://api.sheety.co/b986aa330f6b7bd3394167dfe6964521/flightDeals/prices'
    # .put() sheety_url + [object id]..
    # object id = row number

    tequila_url = 'https//api.tequila.kiwi.com/'
    top_des = tequila_url+'locations/topdestinations'
    API_KEY_TEQUILA = 'Y8yt2oCEvp2YulBfBXIkOr3-34SPcY5J'

    response = requests.get(url=sheety_url)

    #LIST of dictionaries for data in google sheets
    data_list = response.json()


    #adding IATA through sheety through Tequila api
    # for i in range(len(data_list)):
    #     cur_city = data_list[i][['city']]
    #     id = requests.get(url = 'https://api.tequila.kiwi.com/locations/query', json = {'term':cur_city}, headers=API_KEY_TEQUILA)
    #     IATA = id
    #     requests.put(url = sheety_url+f'/{i+1}', json = {'price':{'city':}})
    
    id = requests.get(url = 'https://api.tequila.kiwi.com/locations/query', params = {'term':'vancouver'}, headers='Y8yt2oCEvp2YulBfBXIkOr3-34SPcY5J')

    print(id)