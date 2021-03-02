# Best case: O(N), worst case: O(N^2)
# Compare times depends on the order of the given array
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
	bubbleSort(arr)
	print("After: ", arr)
	print("Compare times: ", compareTimes)

def bubbleSort(arr) :
	isSwap = True
	while isSwap == True: # While array is not sorted
		isSwap = False
		for i in range(0, len(arr)-1): # Stop there because we're evaluating i+1
			global compareTimes # Debug (unnecessary)
			compareTimes += 1
			if (arr[i] > arr[i+1]):
				arr[i], arr[i+1] = arr[i+1], arr[i] #Swap
				printStep(arr) # Debug (unnecessary)
				isSwap = True

def printStep(arr):
	global time
	print("Step",time+1 ,arr)
	time+=1

if __name__ == "__main__":
	main()
