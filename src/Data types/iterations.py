from random import randint

listNums = [ 4, 6, 7, 1,3, 8 , 10, 35, 94]
my_dict = { 'py':'python', 'js':'javascript', 'html5':'html', 'css5':'css', 'react':'react'}
# for i in my_dict.items():
#     print(i)


# sum = 0
# for i in listNums:
#     sum += i
   

# print(sum)

# true_condition = True

# li = [randint(1, 1000) for num in range(1000)]

# i = 0
# target_num = 25
# while i < len(li):
#     if li[i] == target_num:
#         print(f"{target_num} found at index {i}")
#     i += 1


# li = [randint(1, 1000) for num in range(100)]

# target_num = 45
# for i, value in enumerate(len(li)):
#     if value == target_num:
#         print(f"{value} at index: {i}")

# while True:
#     print('Select an option below')
#     print('Press 1')
#     print('Press 1')
#     print('Press 3, to quit')
#     user_input = input('Enter your choice --> ')
#     if int(user_input) == 3:
#         break

list1 = [2, 32, 1, 67, 5, 7]
list2 = ['davvid', 'Eric', 'Lisa', 'Ann', 'Tim', 'Julia']

tuple_list = list(zip(list1, list2))
print(f"this is the combined list {tuple_list}")