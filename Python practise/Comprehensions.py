#This is a one line initialization of a list, tuple or dictionary
x = [x + 4 for x in range(5)]
#We are making a for loop inside the list
print(x)

y = [[1 for y in range(50)] for y in range(2)]
# We are printing 1 5o times in 2 lists.
print(y)

z = {z for z in range(100) if z % 13 == 0}
#Printing all values under 100 that are divisible by 13
print(z)