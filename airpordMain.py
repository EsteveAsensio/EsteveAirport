import airpordController as ai
airpordController = ai.AirpodController()

print("1.- Import an airport")
print("2.- Delete an airport")
print("3.- Add a flight operator to an airport")
print("4.- Delete a flight operator from an airport")
print("5.- List airports by operators")
print("6.- List number of planes by operator")
print("7.- Exit")
try:
    option = int(input("Choose option: "))
    while option != 7:
        if option == 1:
            try:
                importIata = input("Introduce the IATA: ")
                airpordController.importAirpod(importIata)
                print("Import Succesfuly!!!")
            except KeyError:
                print("\n¡The IATA", importIata, "not valid!\n")
        elif option == 2:
            deleteIata = input("Introduce the IATA: ")
            airpord = airpordController.deleteAirpod(deleteIata)
            if airpord == True:
                print("Airpord deleted succesfuly!!!")
            else:
                print("\n¡The IATA",deleteIata,"is incorrect or the list of airpords is empty!\n")
            
        elif option == 3:
            searchIata = input("Introduce the IATA: ")
            name= input("Name of the FlightOperator: ")
            try:
                planes = int(input("Planes of the FlightOperator: "))

                if airpordController.addFlightOperator(searchIata, name, planes):
                    print("Information added succesfuly to the aripord " + searchIata + "!!!")
                else:
                    print("\n¡The IATA",searchIata,"is incorrect or the list of airpords is empty!\n")
            except ValueError:
                print("\n¡The planes need to be an Integer!\n")

        elif option == 4:
            searchIata = input("Introduce the IATA: ")
            name = input("Introduce the name of the Flight operator: ")
            
            if airpordController.deleteFlightOperator(searchIata, name):
                print("Information deleted succesfuly to the aripord " + searchIata + "!!!")
            else:
                print("\n¡The",searchIata,"operator could not be deleted\n")

                     
        elif option == 5:
            listAirpordWithOperators = airpordController.listAirpordsWithOperators()
            if len(listAirpordWithOperators) == 0:
                print("\n¡Doesnt exists any airpord with a Flight Operator!\n")
            else:
                for i in listAirpordWithOperators:
                    print("IATA:",i.getIata())
                    print("\tName:",i.getName())
                    print("\tLocation:",i.getLocation())
                    print("\tCity:",i.getCity())
                    print("\tCountry:",i.getCountry())
                    print("\tWebsite:",i.getWebsite())
                    print("\tPhone:",i.getPhone())
                    print("\tFlight Operators:")
                    for x in i.getFlightOperators():
                        print("\t\tName of the operator:", x.getName())
                        print("\t\tPlanes of the operator:", x.getPlanes(), "\n")

            
        elif option == 6:
            listOption = input("BY: airport / all\n")
            if listOption == "all":
                print("hola")
            elif listOption == "airport":
                print("hola2")
            else:
                print("\n¡Option not valid!\n")


        else:
            print("\n¡Choose a valid option!\n")

        print("1.- Import an airport")
        print("2.- Delete an airport")
        print("3.- Add a flight operator to an airport")
        print("4.- Delete a flight operator from an airport")
        print("5.- List airports by operators")
        print("6.- List number of planes by operator")
        print("7.- Exit")
        option = int(input("Choose option: "))

except ValueError:
    print("\n¡The option needs to be an integer!\n")