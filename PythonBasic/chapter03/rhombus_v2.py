#coding: cp949

while True:
    input_odd = int(input("Ȧ���� �Է��ϼ���(0<-����):"))
    
    if not input_odd: #0 �Է½� ����
        print("������ ���α׷� ����� �̿��� �ּż� �����մϴ�.")
        break

    mid_point = int(input_odd/2) #�� �ﰢ������ ���� ���� �� �� ó�� '*'�� ���� ��ġ

    for i in range(0,input_odd): #�������� �� �밢�� ���̴� �Է¹��� Ȧ����ŭ
        for j in range(0,input_odd): 
            
            #�� �ﰢ�� ���,���� �� ���������
            #�߰���(mid_point)�� �������� i�� Ŀ������ ������ �о����� '*' ���
            if (i<mid_point+1) and (j>=mid_point-i) and (j<=mid_point+i):
                print("*",end='')

            #�Ʒ� �ﰢ�� ���
            #�߰���(mid_point)�� �������� i�� Ŀ������ ������ �������� '*' ���
            elif (i>mid_point) and (j>=i-mid_point) and (j<=input_odd-i+mid_point-1):
                print("*",end='')

            #�ش� ���� �ʴ� ������ ' ' ���
            else:
                print(" ",end='')
        print("")

    
