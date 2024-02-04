#A block of code that only runs when it is called, we can store parameters or arguments

def func():
#def is the keyword followed by any word which can take parameters
    print('x')

func()
#We need not print it. We just have to call the function name to run it
def size(size):
#We are adding an argument for this function
    print(size + " is available")
    return size + ' are available'

size('Large')
size('Medium')
size('Small')
print(size("All"))
#We are providing argumets for the size function
#Note: The argument after return keyword will work only if we print functtion

def passport():
    check = input("Do you have a passport? ").capitalize()
    if check == "Yes":
        print("Please proceed")
    else:
         print("Please provide an aleternative document")
    return

passport()
#The passport() function checks weather the indivisual has a passport or provide additional document
# We can provide optional value by making argument x=None eg. def func(i=None)
# We may or may not provide argument when callling the function using None