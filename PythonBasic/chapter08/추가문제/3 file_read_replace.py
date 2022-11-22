with open('life.txt','r') as file:
    text =  file.read()
    text = text.replace('java','python')
    with open('life2.txt', 'w') as file2:
        file2.write(text)
