def removeDups(linkedlist):
	list = []
	current = linkedlist.head
	while current != None:
		
		if current.getData() not in list:
			list.append(current.getData())
			current = current.getNext()
		else:
			print (current.getData())
			linkedlist.remove(current.getData())
			current = current.getNext()
			
	return linkedlist
	
def main():
	linkedlist = LinkedList()
	a = removeDups(linkedlist)
	print(a.display())
	
main()
