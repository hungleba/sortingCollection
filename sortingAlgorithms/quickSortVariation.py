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

def quickSort(array, i, j):
	if(i >= j):
		return;
	if(i < 0 or i >= len(array) or j >= len(array)):
		return;
	x1 = array[i]
	x2 = array[j]
	if(x2 < x1):
		swap(array, i, j)
		printStep(array, i, j)
		x1 = array[i]
		x2 = array[j]
	p1 = i
	p2 = j
	f1 = i + 1
	f2 = j - 1
	k = i + 1
	while(k <= f2 and f1 <= f2):
		if(array[k] < x1) :
			swap(array, f1, k)
			printStep(array, f1, k)
			swap(array, p1, f1)
			printStep(array, p1, f1)
			p1+=1
			f1+=1
			k+=1
		elif(array[k] == x1):
			swap(array, f1, k)
			printStep(array, f1, k)
			f1+=1
			k+=1
		elif(array[k] > x2):
			swap(array, k, f2)
			printStep(array, k, f2)
			swap(array, p2, f2)
			printStep(array, p2, f2)
			p2-=1
			f2-=1
		elif(array[k] == x2):
			swap(array, f2, k)
			printStep(array, f2, k)
			f2-=1
		else:
			k+=1
	print("After loop:", array)
	quickSort(array, i, p1-1);
	quickSort(array, f1, f2);
	quickSort(array, p2+1, j);

def swap(arr, a, b):
	if (a == b):
		return
	arr[a], arr[b] = arr[b], arr[a]

def printStep(arr, a, b):
	global time
	if (arr[a] != arr[b]):
		print("Step:",time+1,"(swapping",arr[a],arr[b],")",arr)
		time+=1

if __name__ == "__main__":
	main()