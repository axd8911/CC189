'''
Still good to know what is the significance of functions like getNext,getData,setNext,setData, etc. Why cannot we directly handle these in LinkedList class?
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
		#move current all the way to next to bottom, until current val equals to item
		#current == previous.next
		#if find item, previous.setNext(current.next)
		
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
		else: previous.setNext(current.getNext())
	
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
		
		
			

def partition(ll,part):
	l_smaller = LinkedList()
	l_bigger = LinkedList()
	part_in_list = None
	
	current = ll.head
	while current:
		if current.getData() > part:
			l_bigger.add(current.getData())
		if current.getData() <= part:
			l_smaller.add(current.getData())
		current = current.getNext()
		
	current = l_bigger.head
	while current:
		l_smaller.add(current.getData())
		current = current.getNext()
		
	return l_smaller
		

	
def main():
	ll = LinkedList()
	ll.add(5)
	ll.add(3)
	ll.add(6)
	ll.add(2)
	ll.add(1)
	ll.add(8)
	a = partition(ll,6)
	print (a.display())

main()
	
	
	
	
	
	
