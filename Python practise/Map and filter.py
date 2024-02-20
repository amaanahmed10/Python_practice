#Map filter applies a given function to each item of the given iterable(list,tuple,etc)

x = [2,3,4,22,47,37,35]
y = [1,3,5,9]

def add(n,m):

    return n*m

#Syntax: map(fun, iter)

result = map(add, x , y)

print(list(result))

#We can use lambda function as well

mp = map(lambda i,j: i*j, x, y)

print(list(mp))

#Filter function returns the items only which satisfy the given condition
alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','q','v','w','x','y','z']
vovels = ['a', 'e', 'i' , 'o', 'u']
fil = filter(lambda v: v in vovels, alphabets)
# Syntax (function , syntax)
print(list(fil))