file = open('test.txt',mode='w')
file.write('Life is too short')
file.close()

file = open('test.txt',mode='r')
print(file.read())
file.close()