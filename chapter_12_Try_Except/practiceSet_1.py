
def tryBlock():
    try :
        a = 10/5
        b = a+5
        return b;
        print("This line will be executed")
    except ZeroDivisionError : 
        print('A zero division error was encountered')
    except TypeError :
        print("A TypeError occurred")

        # else block is executed when the try statement is executed successfully
    else :
        print("This line will be executed only if no exception was raised")
    finally :
        print("This line will always be executed")


tryBlock()


# Raise exception
a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))

if b == 0:
    raise ZeroDivisionError("Hey our program is not meant to divide numbers by zero")
else :
     print(f"The division a/b is {a/b}")