class Node:
	def __init__(self,initdata):
		self.data = initdata
		self.next = None
	
	def getData(self):
		return self.data
	
	def getNext(self):
		return self.next
	
	def setData(self,newdata):
		self.data = newdata
	
	def setNext(self,newnext):
		self.next = newnext
		
class LinkedList:
	def __init__(self):
		self.head = None
		
	def add(self,item):
		temp = Node(item)
		temp.setNext(self.head)
		self.head = temp
		
	
	def remove(self,item):
		current = self.head
		previous = None
		found = False
		while not found:
			if current.getData() == item:
				found = True
			else:
				previous = current
				current = current.getNext()
				
		if previous == None:
			self.head = current.getNext()
		else:
			previous.setNext(current.getNext())
			
	def isEmpty(self):
		return self.head == None
	
	def search(self,item):
		current = self.head
		found = False
		
		while current != None and not found:
			if current.getData() ==item:
				found = True
				
			else: current = current.getNext()
			
		return found
	
	def display(self):
		list_a = []
		current = self.head
		while current != None:
			list_a.append(current.getData())
			current = current.getNext()
		return list_a
	
	def length(self):
		count = 0
		current = self.head
		while current != None:
			count = count + 1
			current = current.getNext()
		return count
