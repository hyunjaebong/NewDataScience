#coding: cp949

while True:
    input_odd = int(input("홀수를 입력하세요(0<-종료):"))
    
    if not input_odd:
        print("마름모 프로그램 출력을 이용해 주셔서 감사합니다.")
        break

    mid = int(input_odd/2)

    print(' '+"-"*input_odd)
    for i in range(0,input_odd):
        print("|",end='')
        for j in range(0,input_odd):
            if i<mid+1 and j>=mid-i and j<=mid+i:
                print("*",end='')
            elif i>mid and j>=i-mid and j<=input_odd-i+mid-1:
                print("*",end='')
            else:
                print(" ",end='')
        print("|\n",end='')

    print(' '+"-"*input_odd)
