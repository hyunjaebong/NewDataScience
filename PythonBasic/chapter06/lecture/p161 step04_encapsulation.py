class Account:
    __balance = 0
    __accName = None
    __accNo = None

    def __init__(self,bal,name,no):
        self.__balance = bal
        self.__accName = name
        self.__accNo =no

    def getBalance(self):
        return self.__balance, self.__accName, self.__accNo

    def deposit(self,money):
        if money < 0:
            print('금액 확인')
            return
        self.__balance += money

acc = Account(1000,'홍길동','125-152-4125-41')

#acc.__balance
bal =  acc.getBalance()
print('계좌정보:', bal)

acc.deposit(10000)
bal = acc.getBalance()
print('계좌정보:', bal)