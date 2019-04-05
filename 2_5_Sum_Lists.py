'''
Almost the same as Leetcode2
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
		
		

def sumLists(l1,l2):
	current1 = l1.head
	current2 = l2.head
	sum_list = LinkedList()
	go_next = 0
	
	while current1 and current2:
		total = current1.getData() + current2.getData() + go_next
		sum_list.add(total%10)
		go_next = total//10
		current1 = current1.getNext()
		current2 = current2.getNext()
		
		if current1 == None and current2 != None:
			current1 = Node(0)
		if current2 == None and current1 != None:
			current2 = Node(0)
	print (go_next)		
	if go_next == 1:
		sum_list.add(1)
	return sum_list


def main():
	l1 = LinkedList()
	l2 = LinkedList()
	l1.add(5)
	l1.add(3)
	l1.add(6)
	l2.add(9)
	l2.add(6)
	l2.add(8)
	a = sumLists(l1,l2)
	print (a.display())

main()
	
	
	
	
	
	
