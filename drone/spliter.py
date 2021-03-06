#import numpy
#import utils
import tools


def deliver(drone, orderNo, amount, item):
    return str(drone) + " D " + str(orderNo) + " " + str(amount) + " " + str(item)

def load(drone, warehouse, amount, item):
    return str(drone) + " D " + str(warehouse) + " " + str(amount) + " " + str(item)


inputArray = []
orders=[]
warehouses=[]
products=[]
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

    nrOfWarehouses=inputArray[3].split(" ")[0]

    warehousesIn=inputArray[4:int(nrOfWarehouses)*2+4]

    for value in range(0,int(len(warehousesIn)/2)):
        position=warehousesIn[value].split(" ")
        productList=warehousesIn[value+1].split(" ")
        warehouses.append((position,productList))



    nrOrders=inputArray[int(nrOfWarehouses)*2+4]
    ordersIn=inputArray[int(nrOfWarehouses)*2+5:int(nrOrders)*3+int(nrOfWarehouses)*2+5]

    for value in range(0,int(len(ordersIn)/3)):
        position=ordersIn[value*3].split(" ")
        nrOfOrders=ordersIn[value*3+1]
        ordersList=ordersIn[value*3+2].split(" ")
        totalWeigth=0
        for order in ordersList:
            totalWeigth+=int(products[int(order)])
        orders.append((totalWeigth,position,ordersList,value))
    #utils(mapSize,drones,nrTurns,maxPayLoad,nrOfWarehouses,warehouses,nrOfOrders,orders)
    orders.sort(key=lambda tup: tup[0])
    #dronePacking([[x] for x in range(n)])
    print(orders);


    droneBusy = []
    for i in range(int(drones) - 1):
        droneBusy.append((i, 0, 0))

    with open('output.txt', 'w') as o:
        while orders:
            order = orders.pop(0)
            for p in order[2]:
                o.write(load(droneBusy[0][0], 0, 1, p))
            for p in order[2]:
                o.write(deliver(droneBusy[0][0], order[3], 1, p))
            distHome = tools.distance(0,0, order[1][0], order[1][1])
            droneBusy[0][1] = distHome + 2*len(order[2])
            droneBusy[0][2] = distHome
            droneBusy.sort(key=lambda tup: tup[1])
            
def dronePacking(checkList):
    if(checkList):
        print("hej")

def totalWeigth(listOfHouses):
    print("H")