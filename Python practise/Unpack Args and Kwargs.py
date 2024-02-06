x = [1,2,3,433,3132,442]
print(x)
print(*x)
#What the unpack operator does it seperates all the elements from a list or tuple

def dim(length, breadth):
    print(length, breadth)


dims = [(10,15), (20,30), (30,45)]

for di in dims:
    print(*di)
dim(**{'length': 4 , 'breadth': 8 })
#This function has 2 arguments which are given in the list. We can use the values without manually doing anything.
#For dictionaries we have to use ** in order for it to work
dim(**{'breadth': 8, 'length': 4})
#The keys need not be in order for the function to run

def func(*this, **that):
    print(this, that)

func(2,4,1,3,4,56,354, zero=0, one=1)
#The *this takes in all the number arguments while the **that takes all the keyword argumetns and seperates them in a list and a tuple

