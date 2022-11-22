def Adder(x,y):
    add=x+y
    return add
print('add=', Adder(10,20))

print('add=', (lambda x,y:x+y)(10,20))