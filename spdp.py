import random
import matplotlib.pyplot as plt
import math


class tsp(object):
    
    def __init__(self):    
        self.coordinates = []
        self.start = []
        self.mindistance = 0
        self.best = []
        self.hist = 0
        self.buku = dict()
        self.fig = 0
        self.bug = dict()
        
    def setCoordinates(self,c):
        self.coordinates = c 
     
    
    def setStart(self,n):
        self.start = self.coordinates[n]
        self.coordinates.append(self.start)
        
    def distance(self,a,b):
        return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)
    
    
    """
    calculate total traver distance
    """
    
    def alldistance(self,coordinates):
        dis = 0
        for i in range(len(coordinates)-1):
            dis += self.distance(coordinates[i],coordinates[i+1])
        return dis   
    
    
    """
    a rough dynamic programming solution functuin
    """
            
    def dynamic_prog(self):
        memo = dict()
        self.mindistance = self.alldistance(self.coordinates)
        self.hist = self.mindistance
        coordinates = self.coordinates[1:]
        for i in range(500):
            tabu = [self.start]
            dis = 0 
            for j in range(len(coordinates)-1):
                tabu.append(random.sample(coordinates,1)[0])
                tb = str([tabu[j],tabu[j+1]])
                if tb in memo:
                    dis+=memo[tb]
                else:
                    newdis =self.distance(tabu[j],tabu[j+1])
                    memo[tb] = newdis
                    dis+=newdis
                    
            tabu.append(self.start)
            dis += self.distance(tabu[j],tabu[j+1])
            self.bug[str(tabu)] = dis
            if dis<self.mindistance:
                self.mindistance = dis
                self.best = tabu    
               
                
        
        self.buku = memo         
        
    
    """
    function to iterate solving function
    """    
                                   
    def iterate(self,n):
        for i in range(n):
            self.dynamic_prog()
    
    """
    plot the traverse
    """
    def plot_coor(self,c):
        x = []
        y = []
        for i in c:
            x.append(i[0])
            y.append(i[1])
        x.append(self.start[0])
        y.append(self.start[1])
        plt.figure(self.fig)    
        plt.plot(x,y) 
        self.fig+=1
           
        
if __name__ =="__main__":
    sales = tsp()
    """
    input coordinates here
    """
    
    berlin = [[25,230],[525,1000],[580,1175],[650,1130],[1605,620],
   [1220,580],[1465,200],[1530,5],[845,680],[725,370],[145,665],
   [415,635],[510,875],[560,365],[300,465],[520,585],[480,415],
   [835,625],[975,580],[1215,245],[1320,315],[1250,400],[660,180],
   [410,250],[420,555],[575,665],[1150,1160],[700,580],[685,595],
   [685,610],[770,610],[795,645],[720,635],[760,650],[475,960],
   [95,260],[875,920],[700,500],[555,815],[830,485],[1170,65],
   [830,610],[605,625],[595,360],[1740,245],[1340,725]]
    """
    cities = []
    for i in range(20):
        cities.append([random.sample(range(50),1)[0],random.sample(range(50),1)[0]])
    """
    
    cities = []
    for i in range(len(berlin)):
        cities.append(berlin[random.sample(range(len(berlin)),1)[0]])
    
    bench = [[random.randint(0,30),random.randint(0,30)] for i in range(30)]
    
    sales.setCoordinates(berlin)
    sales.setStart(0)
    sales.iterate(50)
    kamus = sales.buku
    
    bug = sales.bug
    awal = sales.alldistance(berlin)
    hasil = sales.mindistance
    tabu = sales.best
    sales.plot_coor(berlin)
    sales.plot_coor(sales.best)



