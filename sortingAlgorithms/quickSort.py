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
	quickSort(arr, 0, len(arr)-1)
	print("After: ", arr)
	print("Compare times:", compareTimes)

def quickSort(arr, i, j):
	if (i >= j):
		return
	if (i < 0 or i >= len(arr) or j >= len(arr)):
		return
	pivotValue = arr[i]
	pivot = i
	f = i + 1 #Index of first item > pivot
	for k in range(f, j+1):
		global compareTimes
		compareTimes+=1
		if (arr[k] < pivotValue):
			arr[f], arr[k] = arr[k], arr[f]
			printStep(arr, f, k)
			arr[pivot], arr[f] = arr[f], arr[pivot]
			printStep(arr, pivot, f)
			pivot+=1
			f+=1
		elif (arr[k] == pivotValue):
			arr[f], arr[k] = arr[k], arr[f]
			printStep(arr, f, k)
			f+=1
	print("After loop:", arr)
	quickSort(arr, i, pivot-1)
	quickSort(arr, f, j)

def printStep(arr, a, b):
	global time
	if (arr[a] != arr[b]):
		print("Step:",time+1,"(swapping",arr[a],arr[b],")",arr)
		time+=1

if __name__ == "__main__":
	main()