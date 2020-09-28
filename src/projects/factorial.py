'''
Factorial:
    * the product of an integer n and all the integers below
    * factorial of 4 = 4 * 3 * 2 * 1 = 24
    * its denoted by the ! after the number, so 5 factorial would be written as 5
    * Facorial of 0 is 1
    * what would be the base case if I do this recursively
'''

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


x = 0
print(f"The value of {x} is {factorial(x)}")

x = 1
print(f"The value of {x} is {factorial(x)}")

x = 5
print(f"The value of {x} is {factorial(x)}")
