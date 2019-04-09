'''
Interesting playing with stacks.
Want to play the game "汉诺塔"? This is the basic idea of that.
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

		


def sortStack(somestack):
	small = Stack()
	large = Stack()
	
	while not somestack.isEmpty():
		current = somestack.pop()
		while not large.isEmpty():
			small.push(large.pop())
			
		while small.isEmpty() == False and current < small.peek():
			large.push(small.pop())
		large.push(current)
	while not small.isEmpty():
		large.push(small.pop())
		
	return large
	
	
	

a = Stack()
a.push(1)
a.push(22)
a.push(13)
a.push(7)
a.push(19)
a.push(13)

print (a.items)
print (sortStack(a).items)



