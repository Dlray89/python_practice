def get_input_from_user():
    result = input('Enter your response here: ')
    return result




print('Welcome to your program. What is your name?')
name_result = get_input_from_user()



print('What did you think of the food you ate today? ')
food_result = get_input_from_user()


print('what TV show ending did you dislike the most? ')
show_results = get_input_from_user()


print(f"the summary of your results name: {name_result}. \n food you ate {food_result}. and show results are {show_results}")