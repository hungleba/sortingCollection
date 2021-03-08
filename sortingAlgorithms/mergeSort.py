# T(N) = 2T(N/2) + N
# T(1) = 1
# Space complexity: O(N)
# -> O(NlogN) includes O(N) merge + logN divides
# Sometimes, Mergesort is combined with Insertion Sort since the 
#   latter works well on tiny arrays. For example, you might use Mergesort 
#   but instead of dividing and combining all the way to 1-element arrays, 
#   you stop at an array of size 16 or less and sort those with Insertion Sort 
#   before combining them back together.

import sys
import random

time = 0 # Debug var
compareTimes = 0 # Debug var

def main():
	arr = []

	#99-1
	for i in range(6, 0, -1):
		arr.append(i)
	random.shuffle(arr)
	print("Before: ", arr)
	mergeSort(arr)
	print("After: ", arr)
	print("Compare times: ", compareTimes)

def mergeSort(arr):
	global divideTimes
	global mergeTimes
	if (len(arr) > 1):
		mid = len(arr)//2
		L = arr[:mid]
		R = arr[mid:]
		mergeSort(L)
		mergeSort(R)
		i = j = k = 0
		# Copy data to temp arrays L[] and R[]
		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1
        # Checking if any element was left
		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1
	
if __name__ == "__main__":
	main()