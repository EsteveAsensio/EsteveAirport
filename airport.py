import flightOperators as fo
class Airport:
    def __init__(self, iata, name, location, city, country, website, phone, flightOperators):
        self.__iata = iata
        self.__name = name 
        self.__location = location
        self.__city = city
        self.__country = country
        self.__website = website
        self.__phone = phone
        self.__flightOperators = []  

    #Get y sets

    def getIata(self):
        return self.__iata
    def getName(self):
        return self.__name
    def getLocation(self):
        return self.__location
    def getCity(self):
        return self.__city
    def getCountry(self):
        return self.__country
    def getWebsite(self):
        return self.__website
    def getPhone(self):
        return self.__phone
    def getFlightOperators(self):
        return self.__flightOperators


    def setIata(self, value):
        self.__name = value
    def setName(self, value):
        self.__name = value
    def setLocation(self, value):
        self.__location = value
    def setCity(self, value):
        self.__city = value
    def setCountry(self, value):
        self.__country = value
    def setWebsite(self, value):
        self.__website = value
    def setPhone(self, value):
        self.__phone = value
    def setFlightOperators(self, value):
        self.__flightOperators = value

    def addFlightOperator(self, name, planes):
        operators = fo.FlightOperators(name, planes)
        self.__flightOperators.append(operators)
