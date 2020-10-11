'''
Step 
'''

def bisection_Search(n, arr):
    # starting index
    start = 0
    #Last index in list
    stop = len(arr) - 1

    while start <= stop:
        #to get the middle mid = start + stop // 2
        mid = (start + stop) // 2
        if n == arr[mid]:
            return f"{n} found at index: {mid}"
        # n greater than value at mid
        elif n > arr[mid]:
            # set start value to mid + 1
            start = mid + 1
        else:
            stop = mid - 1
    print('Starting index', start)
    print('Last index', stop)
    return f"{n} not found in list"

def create_list(max_val):
    arr = []
    for num in range(1, max_val + 1):
        arr.append(num)
    return arr



l = create_list(10)
for num in range(15):
    print(bisection_Search(num, l))