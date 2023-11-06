import airport as ai
import requests
class AirportController:
    def __init__(self):
        self.__listAirports = {}

    def importAirpot(self, iata):
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
            airport = ai.Airport(iata, name, location, city, county, website, phone, flightOperators)
            self.__listAirports[iata] = airport
        except KeyError:
            raise KeyError
        

    def deleteAirpot(self, iata):
        if iata in self.__listAirports:
            self.__listAirports.pop(iata)
            return True
        else:
            return False
        
    def addFlightOperator(self, iata, name, planes):
        if iata in self.__listAirports:
            airport = self.__listAirports[iata]
            airport.addFlightOperator(name, planes)
            return True
        else:
            return False
        
    def deleteFlightOperator(self, iata, name):
        if iata in self.__listAirports:
            airport = self.__listAirports[iata]
            listOperators = airport.getFlightOperators()
            if listOperators != None:
                for i in listOperators:
                    if i.getName() == name:
                        listOperators.remove(i)
                        airport.setFlightOperators(listOperators)
                        return True
            else:
                return False
        else:
            return False

    def listAirpordsWithOperators(self):
        listAirportWithOperators = []
        for x in self.__listAirports.values():
            if x.getFlightOperators() != None and len(x.getFlightOperators()) > 0:
                listAirportWithOperators.append(x)
        return listAirportWithOperators

    def listPlanesAirport(self, iata, name):
        if iata in self.__listAirports:
            airport = self.__listAirports[iata]
            numPlanes = 0
            operatorExistes = False
            for i in airport.getFlightOperators():
                if i.getName() == name:
                    operatorExistes = True
                    numPlanes = i.getPlanes() + numPlanes   

            if operatorExistes:
                return numPlanes
            else:
                return False     
        else:
            return False 
        
        
    def listAllPlanes(self, name):
        planes = 0
        operatorExistes = False
        for i in self.__listAirports.values():
            operator = i.getFlightOperators()
            for x in operator:
                if x.getName() == name:
                    operatorExistes = True
                    planes = planes + x.getPlanes()

        if operatorExistes:
            return planes
        else:
            return False


            