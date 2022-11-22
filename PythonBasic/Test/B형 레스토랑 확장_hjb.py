class Restaurant:
    def __init__(self,name,type):
        self.restaurant_name=name
        self.cuisine_type=type
        self.today_customer=0
        self.number_served=0
    def describe_restaurant(self):
        #정보출력
        print(f'저의 레스토랑 명칭은 {self.restaurant_name}이고 {self.cuisine_type} 전문점입니다.')
    def open_restaurant(self):
        #레스토랑이 열렸다는 메세지 출력
        print(f'저희 {self.restaurant_name} 레스토랑 오픈했습니다. 어서오세요.')

    def restaurant(self):
        #서빙한 고객 숫자 출력
        print(f'서빙한 고객은 {self.today_customer}입니다.')

    def reset_number_served(self):
        #서빙한 고객 숫자를 지정
        self.today_customer = 0
        print(f'손님 카운팅을 0으로 초기화 하였습니다..')

    def increment_number(self,number):
        #서빙한 고객 숫자를 늘림
        self.today_customer += number
        self.number_served += number

    def check_customer_number(self):
        #서빙한 고객 숫자를 확인
        print((f'오늘 총 {self.today_customer}명 손님께서 오셨습니다. (전체 누적 손님:{self.number_served})'))

    def __del__(self):
        print(f'{self.restaurant_name} 레스토랑 문닫습니다.')
        with open("고객서빙현황로그.txt", 'a', encoding='UTF-8') as customer_file:
             customer_file.write("%d\t%d\n" %(self.today_customer, self.number_served) )

name,type=input("레스토랑 이름과 요리 종류를 선택하세요(예 띵호화 중식): ").split(" ")
cl=Restaurant(name,type)
cl.describe_restaurant()

input_opencheck=(input("레스토랑을 오픈하시겠습니까?(y / n): ")).lower()
if input_opencheck[0] == "y":
   cl.open_restaurant()

   while True:
       input_number=input("어서오세요. 몇명이십니까?(초기화:0,입력종료:-1,누적고객확인:p) :")
       if input_number =='p':
           cl.check_customer_number()
       elif int(input_number) == -1:
           break
       elif int(input_number) == 0:
           cl.reset_number_served()
       elif int(input_number) > 0:
           cl.increment_number(int(input_number))
del cl



