class Stack:
	def __init__(self):
		self.items = []
		
	def isEmpty():
		return self.items == []
		
	def pop():
		return self.items.pop()
		
	def push(item):
		return self.items.append(item)
		
	def peek():
		return self.items[-1]
		
class Queue:
	def __init__(self):
		self.items = []
		
	def enqueue(item):
		return self.items.insert(0,item)
		
	def dequeue(item):
		return self.items.pop()
