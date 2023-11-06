class FlightOperators:

    def __init__(self, name, planes):
        self.__name = name 
        self.__planes = planes

    def getName(self):
        return self.__name
    def getPlanes(self):
        return self.__planes
    
    def setName(self, value):
        self.__name = value
    def setPlanes(self, value):
        self.__planes = value