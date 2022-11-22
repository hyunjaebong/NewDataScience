from statistics import mean
from math import sqrt

x=[5,9,1,7,4,6]

class Scattering:
    #생성자
    def __init__(self,x):
        self.x=x

    #메서드
    def var_func(self):
        avg = mean(self.x)
        diff = [(i-avg)**2 for  i in self.x]
        self.var=sum(diff)/(len(self.x)-1)
        return self.var
    #메서드
    def std_func(self):
        st=sqrt(self.var)
        return st

sca=Scattering(x)

var= sca.var_func()
print('분산:', var)

std=sca.std_func()
print('표준편차:',std)