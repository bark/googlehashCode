class utilClass:
    
    def __init__(self, mapSize,drones,nrTurns, numberOfDifrentProducts, products,nrOfWarehouses,warehouses,nrOrders,ordersIn):
        self.mapSize = mapSize
        self.drones = drones
        self.nrTurns = nrTurns
        self.numberOfDifrentProducts = numberOfDifrentProducts
        self.products = products
        self.nrOfWarehouses = nrOfWarehouses
        self.warehouses = warehouses
        self.nrOrders = nrOrders
        self.ordersIn = ordersIn
        
    def setMapSize(self, mapSize):
        self.mapSize = mapSize
        
    def getMapSize(self):
        return self.mapSize
        
    def setDrones(self, drones):
        self.drones = drones
        
    def getDrones(self):
        return self.drones
        
    def setNrTurns(self, nrTurns):
        self.nrTurns = nrTurns
        
    def getNrTurns(self):
        return self.nrTurns
        
    def setNumberOfDifrentProducts(self, numberOfDifrentProducts):
        self.numberOfDifrentProducts = numberOfDifrentProducts
        
    def getNumberOfDifrentProducts(self):
        return self.numberOfDifrentProducts
        
    def setProducts(self, products):
        self.products = products
        
    def getProducts(self):
        return self.products
        
    def setNrOfWarehouses(self, nrOfWarehouses):
        self.nrOfWarehouses = nrOfWarehouses
        
    def getNrOfWarehouses(self):
        return self.nrOfWarehouses
    
    def setWarehouses(self, warehouses):
        self.warehouses = warehouses
        
    def getWarehouses(self):
        return self.warehouses
        
    def setNrOrders(self, nrOrders):
        self.nrOrders = nrOrders
        
    def getNrOrders(self):
        return self.nrOrders
         
    def setOrdersIn(self, ordersIn):
        self.ordersIn = ordersIn
        
    def getOrdersIn(self):
        return self.ordersIn
        
