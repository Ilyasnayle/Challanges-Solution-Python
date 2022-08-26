import time # for time measurement

def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

def InputArray():
    arr = []
    n = int(input("Enter the number of elements: "))
    for i in range(n):
        ele = int(input("Enter the element: "))
        arr.append(ele)
    return arr

def PrintArray(arr):
    for i in arr:
        print(i, end=" ")
    print()

def main():
    start = time.time()
    arr = InputArray()
    PrintArray(arr)
    arr = quicksort(arr)
    end = time.time()
    PrintArray(arr)
    print("Time taken: ", end - start)

if __name__ == "__main__":
    main()
