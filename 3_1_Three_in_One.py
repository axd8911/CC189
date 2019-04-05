'''
Three lists in one list... This is easy in Python

'''


class ThreeInOneStack:
	def __init__(self):
		self.num = 3
		self.items = [[] for i in range(self.num)]
		
	def isEmpty(self):
		return self.items == []
		
	def pop(self,stack_index):
		return self.items[stack_index].pop()
		
	def push(self,stack_index,item):
		return self.items[stack_index].append(item)
		
	def peek(self,stack_index):
		return self.items[stack_index][-1]
		
	def display(self):
		return self.items
		

def main():
	multiple_stack = ThreeInOneStack()
	multiple_stack.push(0,5)
	multiple_stack.push(0,9)
	multiple_stack.push(1,8)
	multiple_stack.push(2,6)
	multiple_stack.push(2,77)
	multiple_stack.push(1,51)
	multiple_stack.push(0,58)
	multiple_stack.pop(0)

	print (multiple_stack.display())

main()
