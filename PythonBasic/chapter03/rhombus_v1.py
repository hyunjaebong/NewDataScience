#coding: cp949

while True:
    input_odd = int(input("Ȧ���� �Է��ϼ���(0<-����):"))
    
    if not input_odd:
        print("������ ���α׷� ����� �̿��� �ּż� �����մϴ�.")
        break

    mid = int(input_odd/2) +1

    for i in range(0,mid):
        for j in range(0,input_odd):
            if (j>=mid-1-i) and (j<=mid-1+i):
                print("*",end='')
            else:
                print(" ",end='')
        print("")
