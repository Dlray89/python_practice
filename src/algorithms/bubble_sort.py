def bubble_sort(num_list):
    '''grab the first elment and compare the second element and see if the first is bigger than the second'''

    '''settign up a boolean to true'''
    swap_happened = True
    '''setting up a while loop for swapping'''
    while swap_happened:
        print(f"Bubble sort status: {num_list}")
        ''' set swap_happened to false so it doesn't go inti an infite loop '''
        swap_happened = False


        '''Enter the for loop'''
        for num in range(len(num_list) - 1):
            '''if the first element is great than the second element'''
            if num_list[num] > num_list[num + 1]:
                swap_happened = True
                num_list[num], num_list[num + 1] = num_list[num + 1], num_list[num]
               
   


li = [3, 23, 67,12,3,5,11,2,6,8]
bubble_sort(li)