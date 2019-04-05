'''
Create a cirluar linked list and test


'''

class Node:
	def __init__(self,initdata):
		self.val = initdata
		self.next = None
		
	def getData(self):
		return self.val
	
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
		#add a node to head
		#the head next is the previous head
		temp = Node(item)
		temp.setNext(self.head)
		self.head = temp
		
	def remove(self,item):

		current = self.head
		previous = None
		found = False
		while not found:
			if current.getValue() == item:
				found = True
			else:
				previous = current
				current = current.getNext()
		
		if previous == None:
			self.head = current.getNext()
		else:
			previous.setNext(current.getNext())
	
	
	def search(self,item):
		found = False
		while not found:
			if current.getData() == item:
				found = True
			else: current = current.getNext()
			
		return found
	
	
	def isEmpty(self):
		return self.head == None
		
	def display(self):
		disp = []
		current = self.head
		while current != None:
			disp.append(current.getData())
			current = current.next
		return disp
		
	def length(self):
		count = 0
		current = self.head
		while current != None:
			count = count + 1
			current = current.getNext()
		return count
	
	
	def delete(self,index):
		count = 0
		current = self.head
		previous = None
		while count != index:
			count = count + 1
			previous = current
			current = current.getNext()
		
		if previous == None:
			self.head = current.getNext()
		else:
			previous.setNext(current.getNext())	
		
		

def loopDetection(l1):
	current = l1.head
	l1_dict = {}
	while current:
		if current in l1_dict:
			return current
		else: 
			l1_dict[current] = 1
			current = current.getNext()
		
		
	

def main():
	l1 = LinkedList()

	l1.add(5)
	l1.add(4)
	l1.add(6)
	l1.add(0)
	l1.add(3)
	l1.add(9)
	l1.head.next.next.next.next.setNext(l1.head.getNext())
	

	a = loopDetection(l1)
	print (a.getData())

main()
	
	
	
	
	
	
