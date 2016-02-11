import numpy

inputArray = []


with open('input/mother_of_all_warehouses.in') as f:
    for line in f:
        inputArray.append(line.rstrip())

    inputVars=inputArray[0].split(" ")
    mapSize=(inputVars[0],inputVars[1])
    drones=inputVars[2]
    nrTurns=inputVars[3]
    maxPayLoad=inputVars[4]
    secondRow=inputArray[1].split(" ")
    numberOfDifrentProducts=secondRow[0]
    products=inputArray[2].split(" ")

    products=inputArray[2].split(" ")
