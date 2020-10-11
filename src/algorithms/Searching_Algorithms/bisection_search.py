def bisection_Search(n, arr):
    start = 0
    stop = len(arr) - 1
    mid = (start + stop) // 2
    if n == arr[mid]:
        return f"{n} found at index: {mid}"
    return f"{n} not found in list"

def create_list(max_val):
    arr = []
    for num in range(1, max_val + 1):
        arr.append(num)
    return arr


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num_to_search = 5
print(bisection_Search(num_to_search, l))