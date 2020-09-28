'''
first thing is to set up a key
Set key to index 1
compare key with index before key
if key less than index swapped them

move key to next index

'''


def insertion_sort(arr):
    print('---insertion sort good to go---')

    key = 1
    compare = 0
    while key < len(arr):
        compare += 1

        for i in range(len(arr) - 1):
            compare += 1
            if arr[key] < arr[i]:
                arr[key], arr[i] = arr[i], arr[key]
                
        key += 1
        print(arr)
    print(f"is compares {compare} times")
   


li = [3, 23, 67,12,3,5,11,2,6,8]
insertion_sort(li)