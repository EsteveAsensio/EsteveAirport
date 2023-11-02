import airpordController as ai
airpordController = ai.AirpodController()

print("1.- Import an airport")
print("2.- Delete an airport")
print("3.- Add a flight operator to an airport")
print("4.- Delete a flight operator from an airport")
print("5.- List airports by operators")
print("6.- List number of planes by operator – (by airport / all)")
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
                infoFlightOperator = input("Informtacion about lightOperator: ")
                if airpordController.addFlightOperator(searchIata, infoFlightOperator):
                     print("Information added succesfuly to the aripord " + searchIata + "!!!")
                else:
                    print("\n¡The IATA",searchIata,"is incorrect or the list of airpords is empty!\n")


            
        elif option == 4:
            print("")
            
        elif option == 5:
            print("")
            
        elif option == 6:
            print("")
            
        else:
            print("\n¡Choose a valid option!\n")

        print("1.- Import an airport")
        print("2.- Delete an airport")
        print("3.- Add a flight operator to an airport")
        print("4.- Delete a flight operator from an airport")
        print("5.- List airports by operators")
        print("6.- List number of planes by operator – (by airport / all)")
        print("7.- Exit")
        option = int(input("Choose option: "))

except ValueError:
    print("\n¡The option needs to be an integer!\n")