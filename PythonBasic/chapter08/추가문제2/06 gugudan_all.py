def gugu(dan):
    for i in range(1,10):
        print(dan * i,end='\t')
def all_gugu():
    for dan in range(2,10):
        gugu(dan)
        print()

dan=input("원하는 단을 입력하세요 (예:2, 전체:all):  ")
if dan=='all':
    all_gugu()
else:
    gugu(int(dan))