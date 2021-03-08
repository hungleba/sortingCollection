# Best case: O(N), worst case: O(N^(3/2))
# Compare times depends on the order of the given array
import sys
import random

time = 0 # Debug var
compareTimes = 0 # Debug var

def main():
	arr = [6,2,3,4,0,1]

	#99-1
	# for i in range(5, 0, -1):
	# 	arr.append(i)
	# random.shuffle(arr)
	print("Before: ", arr)
	while (True):
		k = (int(input("k? ")))
		shellSort(arr, k)
		print("Shell sorting with", k, arr)
		if (k == 1):
			break
	print("Compare times: ", compareTimes)

def shellSort(arr, k) :
	global compareTimes
	for curr in range(k, len(arr)):
		compareTimes += 1
		if arr[curr-k] < arr[curr]: #Assume the left-side array is always sorted
			curr += 1
			continue
		else:
			i = curr
			if (i-k >= 0 and arr[i] >= arr[i-k]):
				compareTimes += 1
			while (i-k >= 0 and arr[i] < arr[i-k]): #Move the unsorted element to the right spot in the left-side
				compareTimes += 1
				arr[i-k], arr[i] = arr[i], arr[i-k] #swap
				i -= k
				printStep(arr)


def printStep(arr):
	global time
	print("Step",time+1 ,arr)
	time+=1

if __name__ == "__main__":
	main()