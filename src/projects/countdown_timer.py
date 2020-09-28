import time

def recursive_countdown_timer(n):
    if n == 0:
        return n
    else:
        print(n)
        time.sleep(1)

        return recursive_countdown_timer(n - 1)
        

def iter_countdown_timer(n):
    while n > 0:
        print(n)
        ''' delay of time at 1 second '''
        time.sleep(1)
        n -= 1
    print(n)

li = 5
print(f"counting down from {li}")
# iter_countdown_timer(li)
print(recursive_countdown_timer(li))