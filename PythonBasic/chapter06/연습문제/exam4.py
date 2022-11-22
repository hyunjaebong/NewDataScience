class Permanent(Employee):
    def __init__(self, name,gi,bonus):
        super().__init__(name)
        self.pay = gi +bonus
class Temporary(Employee):
    def __init__(self,name,time,tpay):
        super().__init__(name)
        self.pay = time * tpay

empType = input("고용형태 선택(정규직<P>, 임시직<T>) : ")
if empType == 'P' or empType =='p' :
    name = input('이름: ')
    gi = int(input('기본급: '))
    bonus = int(input('상여금: '))
    p = Permanent(name, gi, bonus)
    print('='*30)
    print('고용형태: 정규직')
    print('이름:', p.name)
    print('급여: ', format(p.pay, '3,d'))
elif empType == 'T' or empType =='t' :
    name = input('이름: ')
    time = int(input('작업시간: '))
    tpay = int(input('시급: '))
    t = Temporary(name, time, tpay)
    print('='*30)
    print('고용형태: 임시직')
    print('이름:', t.name)
    print('급여: ', format(t.pay, '3,d'))
else:
    print('='*30)
    print('입력 오류')
