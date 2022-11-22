multiline="""안녕하세요, Python 세계로 오신걸 
환영합니다."""

cnt=0
doc=[]
word=[]

for line in multiline.split("\n"):
    doc.append(line)
    for w in line.split(" "):
        word.append(w)
        print(w)
        cnt += 1
print('단어수:', cnt)
print(doc)
print(word)