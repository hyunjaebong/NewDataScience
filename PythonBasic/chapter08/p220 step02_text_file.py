try:
    ftest = open('data/ftest.txt', mode='r')
    full_text = ftest.read()
    print(full_text)
    print(type(full_text))

    ftest = open('data/ftest.txt', mode='r')
    lines = ftest.readlines()
    print(lines)
    print(type(lines))
    print('문단 수:', len(lines))

    docs=[]
    for line in lines:
        print(line.strip())
        docs.append(line.strip())
    print(docs)

    ftest = open('data/ftest.txt', mode='r')
    line = ftest.readlines()
    print(line)
    print(type(line))

except Exception as e:
    print('Error 발생 ',e)
finally:
    ftest.close()


