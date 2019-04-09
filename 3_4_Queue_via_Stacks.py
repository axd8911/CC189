'''
Interesting logics.
Push a item in stack, move all items of this stack to another stack. As a result, the earliest item in stack is now on top, while the newly added one is at the bottom.

'''


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
		

class MyQueue:
	def __init__(self):
		self.popstack = Stack()
		self.pushstack = Stack()
		
	def pop(self):
		while not self.pushstack.isEmpty():
			self.popstack.push(self.pushstack.pop())
		return self.popstack.pop()
	
	
	def push(self,item):
		
		while not self.popstack.isEmpty():
			self.pushstack.push(self.popstack.pop())
		self.pushstack.push(item)
		return self.pushstack
	
	def isEmpty():
		return self.popstack.isEmpty()
	
	
	

a = MyQueue()
a.push(1)
a.push(2)
a.push(3)
a.push(4)
a.push(5)

print (a.pop())
print (a.pop())
print (a.push(6))
print (a.pushstack.items)


