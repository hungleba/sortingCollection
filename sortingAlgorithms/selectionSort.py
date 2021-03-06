# Best case: O(N^2), worst case: O(N^2)
# Compare times = (N^2-N)/2 
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
	selectionSort(arr)
	print("After: ", arr)
	print("Compare times: ", compareTimes)


def selectionSort(arr):
	for i in range(len(arr)):
		minIndex = i
		for j in range(i+1, len(arr)):
			global compareTimes # Debug (unnecessary)
			compareTimes += 1
			if (arr[j] < arr[minIndex]): #Find the minimum element in the right-side array
				minIndex = j
		if (minIndex != i):
			arr[i], arr[minIndex] = arr[minIndex], arr[i] # Swap
			printStep(arr);

def printStep(arr):
	global time
	print("Step",time+1 ,arr)
	time+=1

if __name__ == "__main__":
	main()
