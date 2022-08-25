def BinarySearch(arr, l, r, x):
    if r >= l:
        mid = l + (r - l)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return BinarySearch(arr, l, mid-1, x)
        else:
            return BinarySearch(arr, mid+1, r, x)
    else:
        return -1

def main():
    arr = []
    n = int(input("Enter the number of elements in the array: "))
    for i in range(n):
        arr.append(int(input("Enter the element: ")))
    x = int(input("Enter the element to be searched: "))
    
    result = BinarySearch(arr, 0, n-1, x)
    if result != -1:
        print("Element found at index: ", result)
    else:
        print("Element not found")


if __name__ == "__main__":
    main()


