import airpord as ai
import requests
class AirpodController:
    def __init__(self):
        self.__listAirpods = {}

    def importAirpod(self, iata):
        url = "https://airport-info.p.rapidapi.com/airport"

        querystring = {"iata": iata}
        #VLC

        headers = {
            "X-RapidAPI-Key": "9ce6b7b13amshb7fa76956d29723p1e82f8jsn28537b61e560",
            "X-RapidAPI-Host": "airport-info.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        try:
            data = response.json()
            
            iata = data["iata"]
            name = data["name"]
            location = data["location"]
            city = data["city"]
            county = data["county"]
            website = data["website"]
            phone = data["phone"]
            flightOperators = None
            airpord = ai.Airpord(iata, name, location, city, county, website, phone, flightOperators)
            self.__listAirpods[iata] = airpord
        except KeyError:
            raise KeyError
        
    def deleteAirpod(self, iata):
        if iata in self.__listAirpods:
            self.__listAirpods.pop(iata)
            return True
        else:
            return False
        
    def addFlightOperator(self, iata, info):
        if iata in self.__listAirpods:
            airpord = self.__listAirpods[iata]
            airpord.setFlightOperators(info)
            return True
        else:
            return False