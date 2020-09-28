'''
Going to need a marker which will move through the list on outer loop
set the marker at index[0]

compare marker to the next element.
If the number is smaller to the marker 
Swapped them
go through list until complete

next iteration set market to the next element
and repeat

'''

def selection_sort(arr):
    print('----Selection sort ready to go----')
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
        print(arr)


    


li = [ 4, 87, 2, 7, 10, 20, 44, 3, 6, 1, 203, 5]
selection_sort(li)

