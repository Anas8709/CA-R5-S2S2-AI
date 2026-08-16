'''
this is a math module for more math functionality

'''



def factorial(num:int)->int:
    if num == 0:
        return 0
    if num == 1:
        return 1
    return num * factorial(num -1 )

def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True