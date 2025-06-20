try:
    num = 10 / 0
except ZeroDivisionError:
    print("Can't divide by zero!")


#multiple exceptions
try:
    x = int(input("type a number: "))
    result = 10/x
    print("result: ", result)
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("Can't divide by zero!")


# else finaly
try: 
    num = int(input("enter a number: "))
    print('Square: ', num**2)
except ValueError:
    print('invalid input!')
else: 
    print('opperation successful')
finally:
    print('clean up close file and etc')