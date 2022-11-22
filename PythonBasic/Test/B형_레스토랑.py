class Restaurant:
    def __init__(self, name, types):
        self.restaurant_name = name
        self.cuisine_type = types
        self.today_customer = 0
        self.number_served = 0
        try:
            with open("고객서빙현황로그.txt", 'r', encoding='UTF-8') as customer_f:
                customer_log = ((customer_f.readlines())[-1].split("\t"))[1]
                self.number_served = int(customer_log)
        except FileNotFoundError:
            self.number_served = 0

    def describe_restaurant(self):
        print(f"저희 레스토랑 명칭은 '{self.restaurant_name}'이고 {self.cuisine_type} 전문점입니다.\n")

    def open_restaurant(self):
        print(f"저희 {self.restaurant_name} 레스토랑 오픈했습니다. 어서오세요\n")

    def reset_number_served(self):
        self.today_customer = 0
        print("손님 카운팅을 0으로 초기화 하였습니다.\n")

    def increment_number_served(self, number):
        self.today_customer += number
        self.number_served += number
        print(f"손님 {number}명 들어오셨습니다. 자리를 안내해 드리겠습니다.\n")

    def check_customer_number(self):
        print(f"오늘 총 {self.today_customer}명 손님께서 오셨습니다. (전체 누적 손님: {self.number_served}) \n")

    def __del__(self):
        print(f"{self.restaurant_name} 레스토랑 문닫습니다.")
        with open("고객서빙현황로그.txt", 'a', encoding='UTF-8') as customer_f:
            customer_f.write("%d\t%d\n" % (self.today_customer, self.number_served))


rest_name, rest_type = input("레스토랑 이름과 요리 종류를 선택하세요.(공백으로 구분): ").split(" ")
opening_rest = Restaurant(rest_name, rest_type)
opening_rest.describe_restaurant()
is_open = (input("레스토랑을 오픈하시겠습니까? (y / n): ")).lower()

if is_open[0] == 'y':
    input_num = 0
    opening_rest.open_restaurant()
    while True:
        input_num = input("어서오세요. 몇명이십니까? (초기화:0, 입력종료:-1, 누적고객확인:p) : ")
        if input_num == 'p':
            opening_rest.check_customer_number()
        elif int(input_num) == 0:
            opening_rest.reset_number_served()
        elif int(input_num) == -1:
            break
        elif int(input_num) > 0:
            opening_rest.increment_number_served(int(input_num))

del opening_rest
