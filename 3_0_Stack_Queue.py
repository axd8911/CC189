class Stack:
	def __init__(self):
		self.items = []
		
	def isEmpty(self):
		return self.items == []
		
	def pop(self):
		return self.items.pop()
		
	def push(self,item):
		return self.items.append(item)
		
	def peek(self):
		return self.items[-1]
		
class Queue:
	def __init__(self):
		self.items = []
		
	def enqueue(self,item):
		return self.items.insert(0,item)
		
	def dequeue(self):
		return self.items.pop()
		

a = Stack()
a.push(1)
a.push(2)

a.pop()
a.pop()
a.pop()

print (a.items)
