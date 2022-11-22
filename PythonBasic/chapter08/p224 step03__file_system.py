import os

os.getcwd()

#os.chdir('chapter08')
#os.getcwd()

os.listdir('.')

#os.mkdir('test')
#os.listdir('.')

os.chdir('test')
os.getcwd()

os.makedirs('test2/test3')
os.listdir('.')

os.chdir('test2')
os.listdir('.')

os.rmdir('test3')
os.listdir('.')

os.chdir('../..')
os.getcwd()

os.removedirs('test/test2')