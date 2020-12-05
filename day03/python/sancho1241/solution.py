#import numpy as np

class Toboggan ():
    
    def __init__(self,slope=dict):
        self.STEER_RIGHT=slope["y"]
        self.STEER_DOWN=slope["x"]
        self.position = {"x":0, "y":0} 
        self.treesHit = 0

    def steerRight(self):
        #steering right -> change y-position
        self.position["y"] += self.STEER_RIGHT

    def steerDown(self):
        #steering down -> change x-position
        self.position["x"] += self.STEER_DOWN
    
    def sleighRide(self,myMap):
        
        for x in range(len(myMap.MAP)-1):
            self.steerRight()
            self.steerDown()
            #print(self.position)
            
            #print("toboggan.position:{}".format(self.position))
            #print("Map.Länge.x={}, Map.Länge.y={}".format(len(myMap.MAP),len(myMap.MAP[0])))
            
            #check if end of map is reached and extend map 
            if self.position["y"] >= len(myMap.MAP[0]):
                myMap.extend()  
            
            myMap.setMark(self)

        #print(myMap)
        return self.treesHit

        

class Map ():
    
    def __init__(self,map):
        self.MAP = map
        self.PATTERN = map
        self.SQUARE = '0'
        self.TREE = '#'
        self.HIT = 'X'
    
    def setMark(self,myToboggan):
        x = myToboggan.position["x"]
        y = myToboggan.position["y"]

        myLine = [y for y in self.MAP[x]] 
        if self.MAP[x][y] == self.TREE:
            myLine[y] = self.HIT
            myToboggan.treesHit += 1
        else:
            myLine[y] = self.SQUARE
        self.MAP[x] = "".join(myLine)
    
    def extend(self):
        #self.MAP = self.MAP.append(self.PATTERN)
        #print(len(self.PATTERN))
        #print (self.MAP[0])
        #print (self.PATTERN[0])
        #print (self.MAP[0] + " " + (self.PATTERN[0]))
        #print (self.MAP[0].join(self.PATTERN[0][0]))
        self.MAP = [self.MAP[x] + (self.PATTERN[x]) for x in range(0,len(self.PATTERN))]
        #self.MAP = np.concatenate(self.MAP,self.PATTERN)

    def __str__(self):
        return '\n'.join(self.MAP)

    '''def printMap(self):
        print(self.MAP)'''

    def printPattern(self):
        print(self.PATTERN)

def testToboggan():
    myToboggan = Toboggan()
    print (myToboggan.position)
    for x in range (0,10):
        myToboggan.steerRight()
        myToboggan.steerDown()
        print (myToboggan.position)
    


def parseInput (puzzleInput):
    # read password lines
    myFile = open(puzzleInput, 'r') 
    myList = myFile.read().splitlines()
    #myList = myFile.read()
    #myList = myFile.read().splitlines()
    #myList = [line.splitlines() for line in myList] 
    #print (myList[0][11]) 
    return myList

def solvePuzzlePart1 (myMap):
    
    
    myToboggan = Toboggan({"x":1,"y":3})
    
    #print(myToboggan.position)
    print (myMap)
    treesHit = myToboggan.sleighRide(myMap)
    
    return "Star1: {} trees hit".format(treesHit)

def solvePuzzlePart2 (myMap):
    treesHit = 0 
    slopes = [{"x":1,"y":1},
              {"x":1,"y":3},
              {"x":1,"y":5},
              {"x":1,"y":7},
              {"x":2,"y":1}]
    
    myMaps = [Map(myMap) for slope in slopes]

    for x,slope in enumerate(slopes):
        myToboggan = Toboggan(slope)
        print (myMap)
        treesHit *= myToboggan.sleighRide(myMaps[x])
        print (treesHit)
    return "Star2: all in all {} trees hit".format(treesHit)

myList = parseInput('testinput.txt')
myMap = Map(myList)
print(solvePuzzlePart1(myMap)) 
print(solvePuzzlePart2(myMap)) 

