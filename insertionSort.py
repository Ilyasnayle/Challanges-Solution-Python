import time
def InsertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def InputArray():
    arr = []
    n = int(input("Enter the number of elements: "))
    for i in range(n):
        ele = int(input("Enter the element: "))
        arr.append(ele)
    return arr

def main():
    arr = InputArray()
    start = time.time()
    arr = InsertionSort(arr)
    end = time.time()
    print("Sorted array: ", arr)
    print("Time taken: ", end - start)

if __name__ == "__main__":
    main()
