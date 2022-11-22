string = """나는 홍길동 입니다.
주소는 서울시 입니다.
나이는 35세 입니다."""

sents = []
words = []

for sen in string.split(sep="\n") :
    sents.append(sen)

    for word in sen.split(): #sen을 다시 공백으로 잘라라
        words.append(word)   #담아라.
print('문장:', sents)
print('문장수:', len(sents))
print('단어:', words)
print('문어수:', len(words))
