class SetofStack:

	def __init__(self,maximum):
		self.items = [[]]
		self.threshold = maximum
	
	def push(self,item):
		if len(self.items[-1]) == self.threshold:
			return self.items.append([item])
		else:
			return self.items[-1].append(item)
			
	def pop(self):
		
		pop_out = self.items[-1].pop()
		if self.items[-1] == [] and len(self.items) > 1:
			del self.items[-1]
		return pop_out
	

a = SetofStack(5)
a.push(1)
a.push(2)


print (a.items)
