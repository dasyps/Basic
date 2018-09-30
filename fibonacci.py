import functools

while True:
    try:
        userinput=input('Enter the fibonacci number for which we need to get you value:')
        fibnum=int(userinput)
        break
    except ValueError:
        print('invalid entry')
    except KeyboardInterrupt:
        print('invalid typing')  

print("You entered :",fibnum)

@functools.lru_cache()
def fib_calc(mynum):
    if mynum < 2:
        return mynum
    else:

        y = fib_calc(mynum - 2) + fib_calc(mynum - 1)
        print(mynum,y)
    return y

fibfinal=fib_calc(fibnum)
print("Fibonacci number for position",fibnum,"is",fibfinal)