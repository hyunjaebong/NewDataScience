#coding: cp949

while True:
    input_odd = int(input("Ȧ���� �Է��ϼ���(0<-����):"))
    
    if not input_odd:
        print("������ ���α׷� ����� �̿��� �ּż� �����մϴ�.")
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
