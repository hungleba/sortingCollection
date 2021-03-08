class Node:
	def __init__(self, val, next, prev):
		self.val = val
		self.next = next
		self.prev = prev
node1 = Node(6, None, None)
def main():
	#6,2,3,4,0,1
	#node1 = Node(6, None, None)
	node2 = Node(2, None, None)
	node3 = Node(3, None, None)
	node4 = Node(4, None, None)
	node5 = Node(0, None, None)
	node6 = Node(1, None, None)
	#Construct ll
	node1.next = node2
	node2.prev = node1
	node2.next = node3
	node3.prev = node2
	node3.next = node4
	node4.prev = node3
	node4.next = node5
	node5.prev = node4
	node5.next = node6
	node6.prev = node5
	#Sorting
	head = node1
	printll(head)
	print()
	insertionSort(head, 0, None)
	print()
	printll(head)

def insertionSort(currNode, flag, checkingNode):
	global node1
	printll(node1)
	if currNode is not None:
		if (flag == 0):
			if (currNode.next is not None and currNode.val > currNode.next.val):
				currNode.val, currNode.next.val = currNode.next.val, currNode.val
				insertionSort(currNode.next, 1, currNode)
			else:
				insertionSort(currNode.next, 0, None)
		else:
			if (checkingNode.prev == None or checkingNode.prev.val <= checkingNode.val):
				insertionSort(currNode, 0, None)
			else:
				checkingNode.prev.val, checkingNode.val = checkingNode.val, checkingNode.prev.val
				insertionSort(currNode, 1, checkingNode.prev)

def printll(head):
	hd = head
	while (hd != None):
		print(hd.val, end = " ")
		hd = hd.next
	print()

if __name__ == "__main__":
	main()
