def returnKth(list,k):
	current = list.head
	count = 0
	while count < k-1:
		
		current = current.getNext()
		count = count + 1
	return current.getData()
	
def main():
	linkedlist = LinkedList()
	linkedlist.add(1)
	linkedlist.add(2)
	linkedlist.add(3)
	linkedlist.add(4)
	linkedlist.add(5)
	linkedlist.add(6)
	linkedlist.add(7)
	linkedlist.add(8)
	linkedlist.add(9)
	a = returnKth(linkedlist, 9)

	print(a)
	
main()
