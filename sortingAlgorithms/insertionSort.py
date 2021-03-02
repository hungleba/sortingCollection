# Best case: O(N), worst case: O(N^2)
# Compare times depends on the order of the given array
# Note: a better version of bubbleSort, often used when n is small.
import sys
import random

time = 0 # Debug var
compareTimes = 0 # Debug var

def main():
	arr = []

	#99-1
	for i in range(5, 0, -1):
		arr.append(i)
	random.shuffle(arr)
	print("Before: ", arr)
	insertionSort(arr)
	print("After: ", arr)
	print("Compare times: ", compareTimes)

def insertionSort(arr) :
	global compareTimes
	for curr in range(0, len(arr)-1):
		compareTimes += 1
		if arr[curr] < arr[curr+1]: #Assume the left-side array is always sorted
			curr += 1
			continue
		else:
			i = curr+1
			if (i != 0 and arr[i] >= arr[i-1]):
				compareTimes += 1
			while (i != 0 and arr[i] < arr[i-1]): #Move the unsorted element to the right spot in the left-side
				compareTimes += 1
				arr[i-1], arr[i] = arr[i], arr[i-1] #swap
				i -= 1
				printStep(arr)


def printStep(arr):
	global time
	print("Step",time+1 ,arr)
	time+=1

if __name__ == "__main__":
	main()