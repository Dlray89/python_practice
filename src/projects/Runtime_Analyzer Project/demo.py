print("Algorithms file loaded")

def quicksort(nums):
    ''' Set up the base case if length of nums is less than 2 '''
    if len(nums) < 2:
        ''' return nums list'''
        return nums
    else:
        ''' set up pivot point '''
        pivot = nums[-1]
        ''' set up empty list naming them smaller,equal and larger '''
        smaller, equal, larger = [], [], []
        ''' for every num in list '''
        for num in nums:
            ''' if num is lesser than the pivot point '''
            if num < pivot:
                ''' append to smaller list '''
                smaller.append(num)
                ''' else if num is equal to pivot '''
            elif num == pivot:
                ''' append to equal list '''
                equal.append(num)

            else:
                ''' else put larger elements in larger list '''
                larger.append(num)
                ''' returun all list  '''
        return quicksort(smaller) + equal + quicksort(larger)


def merge_sorted(arr1, arr2):
    sorted_arr = []
    i, j = 0, 0
    while i < len(arr1)  and j < len(arr2):
      
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1
        else:
            sorted_arr.append(arr2[j])
            j += 1
    while i < len(arr1):
        sorted_arr.append(arr1[i])
   
        i += 1
    while j < len(arr2):
    
        sorted_arr.append(arr2[j])
        j += 1
   
    return sorted_arr


def mergesort(arr):
    if len(arr) < 2:
        return arr[:]
    else:
        middle = len(arr) //2
        l1 = mergesort(arr[:middle])
        l2 = mergesort(arr[middle:])
        return merge_sorted(l1,l2)


def bubble_sort(num_list):
    '''grab the first elment and compare the second element and see if the first is bigger than the second'''

    '''settign up a boolean to true'''
    swap_happened = True
    '''setting up a while loop for swapping'''
    while swap_happened:
      
        ''' set swap_happened to false so it doesn't go inti an infite loop '''
        swap_happened = False


        '''Enter the for loop'''
        for num in range(len(num_list) - 1):
            '''if the first element is great than the second element'''
            if num_list[num] > num_list[num + 1]:
                swap_happened = True
                num_list[num], num_list[num + 1] = num_list[num + 1], num_list[num]


def insertion_sort(arr):

    key = 1
    compare = 0
    while key < len(arr):
        compare += 1

        for i in range(len(arr) - 1):
            compare += 1
            if arr[key] < arr[i]:
                arr[key], arr[i] = arr[i], arr[key]
                
        key += 1


def selection_sort(arr):
    ''' setting up marker at the first index'''
    marker = 0

    ''' while marker is less than the len(arr) '''
    while marker < len(arr):

        ''' enter the for loop '''
        for i in range(len(arr)):
            ''' if the element at index[i] is greater than the element at the marker '''
            if arr[i] > arr[marker]:
                ''' swap elements arr[marker], arr[i] '''
                arr[marker], arr[i] = arr[i], arr[marker]
        ''' increment market by 1 '''        
        marker += 1