'''
It takes time to implement two linked lists as example, thus no example here..
The tips in CC189 provides a full picture of "intersection" of linked lists, it may help you to understand the conception and reduce the complexicity in number, not in scale.


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
		
		

def intersection(l1,l2):
	l1_count = 0
	l1_dict = {}
	l1_current = l1.head
	inter = None
	while l1_current:
		l1_dict[l1_current] = l1_count
		l1_current = l1_current.getNext()
		l1_count = l1_count + 1

	l2_count = 0
	l2_current = l2.head
	found = False
	while l2_current and not found:
		if l2_current in l1_dict:
			found = True
			inter = l2_current
		else:
			l2_current = l2_current.getNext()
			l2_count = l2_count + 1
			
			
	return inter 
		
	

def main():
	l1 = LinkedList()
	l2 = LinkedList()
	l1.add(5)
	l1.add(3)
	l1.add(6)
	l2.add(0)
	l2.add(3)
	l2.add(5)	

	a = intersection(l1,l1)
	print (a.getData())

main()
	
	
	
	
	
	
