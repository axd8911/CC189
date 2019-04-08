class Stack:
	def __init__(self):
		self.items = []
		self.min = None
		
	def isEmpty(self):
		return self.items == []
		
	def pop(self):
		return self.items.pop()
		
	def push(self,item):
		if self.min == None:
			self.min = item
		elif self.min > item:
			self.min = item
		return self.items.append(item)
		
	def peek(self):
		return self.items[-1]
		
	def min(self):
		return self.min
		

def main():
	multiple_stack = Stack()
	multiple_stack.push(57)
	multiple_stack.push(9)
	multiple_stack.push(8)
	multiple_stack.push(5)
	multiple_stack.push(77)
	multiple_stack.push(51)
	multiple_stack.push(58)
	multiple_stack.pop()

	print (multiple_stack.min)

main()
