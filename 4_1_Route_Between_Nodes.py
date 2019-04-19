class Vertex:
	def __init__(self,key):
		self.id = key
		self.connectedTo = {}
	
	def addNeighbor(self,nbr,weight=0):
		self.connectedTo[nbr] = weight
	
	def __str__(self):
		return str(self.id) + 'connected to' + str([x.id for x in self.connectedTo]) 
		
	def getConnections(self):
		return self.connectedTo.keys()

	def getID(self):
		return self.id

	def getWeight(self,nbr):
		return self.connectedTo[nbr]

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
			
	def __contains__(self,n):
		return n in self.vertList

	def addEdge(self,f,t,cost=0):
		if f not in self.vertList:
			nv = self.addVertex[f]
		if t not in self.vertList:
			nv = self.addVertex[t]
		self.vertList[f].addNeighbor(self.vertList[t],cost)

	def getVertices(self):
		return self.vertList.keys()

	def __iter__(self):
		return iter(self.vertList.values())


def routeBetweenNodes(node1,node2,graph):
	passed = {node1}
	current = node1.connectedTo
	
	while node2 not in current and current != {}:
		current2 = {}
		for item1 in current:
			for item2 in item1.connectedTo:
				if item2 not in passed:
					current2[item2] = 0
		if node2 in current2:
			return True
		else:
			current = current2.copy()
			
	return False
		
	
	

	
g = Graph()

for i in range(7):
	g.addVertex(i)
	

g.addEdge(0,2,0)
g.addEdge(2,5,0)
g.addEdge(5,1,0)
g.addEdge(1,6,0)
g.addEdge(1,3,0)
g.addEdge(3,4,0)
print (g)

print (routeBetweenNodes(g.vertList[1],g.vertList[2],g))
