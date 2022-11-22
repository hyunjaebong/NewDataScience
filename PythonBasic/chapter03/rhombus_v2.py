#coding: cp949

while True:
    input_odd = int(input("홀수를 입력하세요(0<-종료):"))
    
    if not input_odd: #0 입력시 종료
        print("마름모 프로그램 출력을 이용해 주셔서 감사합니다.")
        break

    mid_point = int(input_odd/2) #위 삼각형으로 볼때 높이 및 맨 처음 '*'가 찍힐 위치

    for i in range(0,input_odd): #마름모의 각 대각선 길이는 입력받은 홀수만큼
        for j in range(0,input_odd): 
            
            #위 삼각형 모양,가장 긴 가로축까지
            #중간점(mid_point)을 기준으로 i가 커질수록 범위가 넓어지며 '*' 출력
            if (i<mid_point+1) and (j>=mid_point-i) and (j<=mid_point+i):
                print("*",end='')

            #아래 삼각형 모양
            #중간점(mid_point)을 기준으로 i가 커질수록 범위가 좁아지며 '*' 출력
            elif (i>mid_point) and (j>=i-mid_point) and (j<=input_odd-i+mid_point-1):
                print("*",end='')

            #해당 하지 않는 범위는 ' ' 출력
            else:
                print(" ",end='')
        print("")

    
