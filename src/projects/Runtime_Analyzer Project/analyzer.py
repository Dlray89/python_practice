import random
from demo import quicksort, mergesort, bubble_sort, insertion_sort, selection_sort
from time import time
''' 

Specifications

* Generate list of random integers according to specifications

* List size will be specified by user at run time

* Range of integer values will be specfied by user at  run time

* Run function with gerated list of integers

* CAlculate and display the time it took to run the function

* Allow for multiple runs
'''
def create_random_list(size, max_value):
    ''' A fucntion used to create a list of random integers '''
    # Create empty list 
    random_list = []
    # Set up a range of random integers
    for i in range(size):
        # Append integers in random list using random and randint
        random_list.append(random.randint(1,max_value))
        # return the list
    return random_list

def analyzeFunction(func_name, arr):
    # set up start time
    Start = time()
    # the name of fuction goes here along with list
    func_name(arr)
    # set up end time
    end = time()
    # end - start for elapsed time
    seconds = end - Start
    print(f"{func_name.__name__.capitalize()}\t-> Elapsed Time: {seconds: .5f}")



''' Set up user input here for size and max value of the list user wants to create '''

size = int(input("What size list do you want to create? "))
max_value = int(input("What is the max value of the range? "))
run_time = int(input("How many times do you want to run? "))

for num in range(run_time):
    print(f"Run: {num+1}")
    l = create_random_list(size, max_value)

    analyzeFunction(quicksort, l)
    analyzeFunction(mergesort, l)
    analyzeFunction(bubble_sort, l.copy())
    analyzeFunction(insertion_sort, l)
    analyzeFunction(selection_sort, l)
    analyzeFunction(sorted, l)
    print("-" * 40)
    
