def print_array(arr):
    for val in arr:
        print(val,end=" ")
    print()

def selection_sor(arr):
    n = len(arr)    
    for i in range(n-1):
        min_idx = i
        for j in range(i+1,n):
            if arr[j] < arr[min_idx]:
                min_idx = j;
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

if __name__ == "__main__":
    arr = [64,25,12,22,11]

    print ("original array:", end="")
    print_array(arr)

    selection_sor(arr)

    print("sorted array:",end="")
    print_array(arr)

