import numpy

inputArray = []


with open('input/logo.in') as f:
    for line in f:
        inputArray.append(line.rstrip())
    inputVars=inputArray[0]
    inputArray = numpy.delete(inputArray, (0), axis=0)
#    print(inputArray)

    for rowIndex,row in enumerate(inputArray):
        for colIndex,point in  enumerate(row):
            print(rowIndex, colIndex)



def queThing(checkList,chosenOnes,inputVars):
    global inputArray    # Needed to modify global copy of globvar
    print str
    return
