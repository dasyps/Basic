while True:
    try:
        userinput=input('Enter your age:')
        age=int(userinput)
        break
    except ValueError:
        print('invalid entry')
    except KeyboardInterrupt:
        print('invalid typing')  

newage = age
age = age + 10
print('your age=',age)
print('your newage=',newage)
