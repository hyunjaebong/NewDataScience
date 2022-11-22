#객체 지향 다형성
# (4) 다형성
flight.fly() # 날다, fly 원형 메서드

flight = air
flight.fly() # 비행기가 날다.

flight = bird
flight.fly() # 새가 날다.

flight = paper
flight.fly() # 종이 비행기가 날다.

#사용자는 어느 자식 인스턴스의 fly를 사용하는지 몰라도 됨.
#공통 규격(flight)의 fly만 알면됨
#마치 부품 교체하듯이 필요에 따라 바꾸기만 하면서
#fly() 함수만 사용하면 됨.
#이렇게 하여 다양한 자식 클래스에서 정의된 함수를 필요할 때 마다 선택하여 사용함
#이것을 통해 다형성을 구현!