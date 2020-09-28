'''
divider this list in half until we get to idndiviual numbers
[3,7,9,6,10,23,44,1,2,4,1]
Split orginal list in two
[3,7,9,6,10] [23,44,1,2,4,1]
split left list in two
[3,7,9,6,10]
[3,7] [9,6,10]
split left list again
[3][7]
3 and 7 is return
compare first elment to second elment
if first is less than second swapped them and merged them

continue to the right list
[9,6,10]
[9][6,10]
'''

def merge_sort(arr1, arr2):
    print('merge function called with list below')
    print(f"left {arr1} and right {arr2}")
    sorted_arr = []
    i, j = 0, 0
    while i < len(arr1)  and j < len(arr2):
      
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1
        else:
            sorted_arr.append(arr2[j])
            j += 1
        print(sorted_arr)
    while i < len(arr1):
        sorted_arr.append(arr1[i])
   
        i += 1
    while j < len(arr2):
    
        sorted_arr.append(arr2[j])
        j += 1
   
    return sorted_arr


def divide_arr(arr):
    if len(arr) < 2:
        print(f"Base condition reached with: {arr[:]}")
        return arr[:]
    else:
        middle = len(arr) //2
        print("current list to work with: ", arr)
        print("Left split: ", arr[:middle])
        print("Right split: ", arr[middle:])
        l1 = divide_arr(arr[:middle])
        l2 = divide_arr(arr[middle:])

# li = [2,4,6,8,88,100,102]
# li2 = [1,3,5,7,9,10,87,44]
# print(f"merged list: {merge_sort(li, li2)}")

l1 = [4,2,1,67]
divide_arr(l1)