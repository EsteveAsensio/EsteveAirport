import airpord as ai
import requests
class AirpodController:
    def __init__(self):
        self.__listAirpords = {}

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
            self.__listAirpords[iata] = airpord
        except KeyError:
            raise KeyError
        

    def deleteAirpod(self, iata):
        if iata in self.__listAirpords:
            self.__listAirpords.pop(iata)
            return True
        else:
            return False
        
    def addFlightOperator(self, iata, name, planes):
        if iata in self.__listAirpords:
            airpord = self.__listAirpords[iata]
            airpord.addFlightOperator(name, planes)
            return True
        else:
            return False
        
    def deleteFlightOperator(self, iata, name):
        if iata in self.__listAirpords:
            airpord = self.__listAirpords[iata]
            listOperators = airpord.getFlightOperators()
            if listOperators != None:
                for i in listOperators:
                    if i.getName() == name:
                        airpord.getFlightOperators().remove(i)
                
                if len(listOperators) != len(airpord.getFlightOperators()):
                    airpord.setFlightOperators(listOperators)
                    return True
                else:
                    #No se ha eliminado ninguna operador de vuelo
                    return False
            else:
                return False
        else:
            return False
    

    def listAirpordsWithOperators(self):
        listAirpordWithOperators = []
        for x in self.__listAirpords.values():
            if x.getFlightOperators() != None or len(x.getFlightOperators()) != 0:
                listAirpordWithOperators.append(x)
        return listAirpordWithOperators


