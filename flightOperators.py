class FlightOperators:

    def __init__(self, name, planes) -> None:
        self.__name = name 
        self.planes = planes

    def getName(self):
        return self.__name
    def getPlanes(self):
        return self.planes
    
    def setName(self, value):
        self.__name = value
    def setPlanes(self, value):
        self.planes = value