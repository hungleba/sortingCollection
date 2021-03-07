# Best case, worst case: O(NlogN)
# Popular when space is tight (e.g. embedded systems) because it provides 
#   optimal performance with just a few dozen lines of code
import sys
import random

time = 0 # Debug var
compareTimes = 0 # Debug var
step = 0

def main():
	arr = []

	#99-1
	for i in range(6, 0, -1):
		arr.append(i)
	random.shuffle(arr)
	print("Before: ", arr)
	heapSort(arr)
	print("After: ", arr)
	print("Compare times: ", compareTimes)

def heapSort(arr):
	global step
	n = len(arr)
	for i in range(n//2-1, -1, -1):
		heapify(arr, n, i)
	print()
	for i in range(n-1, 0, -1):
		arr[0], arr[i] = arr[i], arr[0]
		step+=1
		print("Step",step,arr)
		heapify(arr, i, 0)

def heapify(arr, n, i):
	global step
	global compareTimes
	largest = i
	left = i*2+1
	right = i*2+2
	if (left < n):
		compareTimes+=1		# For debugging only
		if (arr[largest] < arr[left]):
			largest = left
	if (right < n):
		compareTimes+=1	
		if (arr[largest] < arr[right]):
			largest = right
	compareTimes+=1
	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i]
		step+=1
		print("Step",step,arr)
		heapify(arr,n,largest)

if __name__ == "__main__":
	main()