from statistics import mean
from math import  sqrt

data={4,5,3.5,2.5,6.3,5.5}

def scattering_func(data):
    dataSet = data

    def avg_func():
        avg_val=mean(dataSet)
        return avg_val

    def var_func(avg):
        diff=[(data-avg)**2 for data in dataSet]
        print(sum(diff))
        var_val =sum(diff)/(len(dataSet)-1)
        return var_val

    def std_func(var):
        std_val = sqrt(var)
        return std_val
    return avg_func, var_func, std_func

    print('평균:', avg())
    print('분산: ',var(avg()))
    print('표준편차', std(var(avg())))