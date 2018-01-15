class Vertex:
    def __init__(self,key):
        self.id = key
        
        self.Color = 'white'
        self.Pred = None
        self.Distance = 0
        
        self.connectedTo = {}
      
        
    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight
        
    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])
        
    def getConnections(self):
        return self.connectedTo.keys()
    def getId(self):
        return self.id
    def getWeight(self,nbr):
        return self.connectedTo[nbr]
    
    def setDistance(self,Distance):
        self.Distance = Distance
    def getDistance(self):
        return self.Distance
    def setPred(self,Pred):
        self.Pred = Pred
    def getPred(self):
        return self.Pred
    def setColor(self,Color):
        self.Color = Color
    def getColor(self):
        return self.Color
    


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex
    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
    def __getitem__(self,key):
        return self.get(key)
    def __contains__(self):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t],cost) 
    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

    

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items) 


'''    
a = Vertex('a')
b = Vertex('b')
c = Vertex('c')

a.addNeighbor(b)
a.addNeighbor(c)

print str(a)


g = Graph()
for i in range(6):
    g.addVertex(i)
print g.vertList

g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)

for v in g:
    for w in v.getConnections():
        print "(%s,%s)" % (v.getId(),w.getId())

'''
        



def buildGraph(wordFile):
    d = {}
    g = Graph()
    wfile = open(wordFile,'r')
    for line in wfile:
        word = line[:-1]
        
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
                
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1,word2)
    return g

def bfs(g,start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while (vertQueue.size()>0):
        currentVert = vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if (nbr.getColor() == 'white'):
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance()+1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor('black')


print buildGraph('wordFile.txt')                
g = buildGraph('wordFile.txt')

for v in g:
    for w in v.getConnections():
        print "(%s,%s)" % (v.getId(),w.getId())
        
start =  g.vertList['fool']

bfs(g,start)

print g.getVertex('sage').getColor()

print str(g.getVertex('sage'))


def traverse(y):
    x = y
    while (x.getPred()):
        print (x.getId())
        x = x.getPred()
    print (x.getId())

traverse(g.getVertex('sage'))

            
