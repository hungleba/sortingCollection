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
	for i in range(15, 0, -1):
		arr.append(i)
	random.shuffle(arr)
	print("Before: ", arr)
	heapSortIndex(arr, 1, 5)
	print("After: ", arr)
	print("Compare times: ", compareTimes)

def heapSortIndex(arr, begin, end):
    global step
    n = len(arr)
    for i in range(begin+((end-begin+1)//2), begin-1, -1):
        heapify(arr, i, begin, end)
    print()
    count = 0;
    for i in range(end, begin, -1):
        arr[begin], arr[i] = arr[i], arr[begin]
        count+=1;
        step+=1
        print("Step",step,arr)
        heapify(arr, begin, begin, end-count)

def heapify(arr, i, begin, end):
	global step
	global compareTimes
	largest = i
	left = ((i-begin)*2+1)+begin
	right = ((i-begin)*2+2)+begin
	if (left < begin+end):
		compareTimes+=1		# For debugging only
		if (arr[largest] < arr[left]):
			largest = left
	if (right < begin+end):
		compareTimes+=1	
		if (arr[largest] < arr[right]):
			largest = right
	compareTimes+=1
	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i]
		step+=1
		print("Step",step,arr)
		heapify(arr, largest, begin, end)

if __name__ == "__main__":
	main()
