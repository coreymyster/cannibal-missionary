class Vertex:
    def __init__(self,key):
        self.id = key            # Typically a string
        self.connectedTo = {}    # dictionary to keep track of the vertices in which its connected, plus weight

    def addNeighbor(self,nbr,weight=0):    # adds a connection from this current vertex to another
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()    # returns verticies in the adjacency list represent by connectedTo

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]    # returns weight of the edge of this vertex
    
    
class Graph:
    def __init__(self):               # initializes the graph itself and creates an empty list of vertices
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):          # creates a new vertex and calls the Vertex class
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):           # checks if edge point is not in the existing verticy list
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())
    
    def __repr__(self):
        return str(self.vertList)


# declare the graph
g = Graph()
    
# possible moves for this game are added into a list
possibleMoves = ["331", "330", "231", "230", "321", "320", "221", "220", "231", "121", "120", "111", "110", "011", "010", "101", "100", "000"]

# creates vertices for each move in the game
for i in possibleMoves:
    g.addVertex(i)

# we connect each possible move in the game with eachother using the for loop below
for i in possibleMoves:
    for n in possibleMoves:
        if n != i:
            g.addEdge(str(i), str(n))

# for testing purposes we're checking the vertices that exist
for v in g:
    print(v)


# the code below is for testing purposes
combinations = g.getVertices()

boatState = 0

print(g.vertList)

for v in g:
    #print(v.__str__())
    for w in v.getConnections():
        print("( %s , %s )" % (v.getId(), w.getId()))
        
