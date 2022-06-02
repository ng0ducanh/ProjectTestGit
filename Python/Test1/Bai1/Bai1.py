from asyncio.windows_events import NULL
import math

def check_perfect_number(num):
    total = 0
    for i in range(1, math.ceil(num/2) +1):
        if num%i == 0:
            total += i
    if num == total:
        return num
    return NULL
    
def write_perfect_number(number):
    arr = []
    for i in range(2,number+1):
        if check_perfect_number(i) != NULL:
            arr.append(check_perfect_number(i))
    return arr

while True:
    try:
        a = int(input("Enter number: "))
        if a >= 0 :
            if len(write_perfect_number(a)) > 0:
                print("The perfect numbers from 0 to " + str(a) + ":")
                for i in write_perfect_number(a):
                    print(i)
            else:
                print("Don't have perfect number from 0 to " + str(a) )
            break
        else:
            print("Number must be positive.")
    except Exception as e :
        print("Number must be a positive number.")
        