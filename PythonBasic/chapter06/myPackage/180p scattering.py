from statistics import mean
from math import  sqrt

def Avg(data):
    avg = mean(data)
    return avg

def var_sd(data):
    avg = Avg(data)
    diff = [(d-avg)**2 for d in data]
    var = sum(diff) / (len(data)-1)
    sd=sqrt(var)
    return  var,sd

if __name__ == "__main__":
    data = [1,3,5,7]
    print('평균=', Avg(data))
    var, sd = var_sd(data)
    print('분산=', var)
    print('표준편차=', sd)