import chapter06.myPackage.scattering
data=[1,3,1.5,2,1,3.2]

print('평균: ', chapter06.myPackage.scattering.Avg(data))

var,sd =  chapter06.myPackage.scattering.var_sd(data)
print('분산:', var)
print('표준편차:', sd)

from  chapter06.myPackage.scattering import Avg, var_sd

print('평균: ', Avg(data))

var,sd=var_sd(data)
print('분산:', var)
print('표준편차:', sd)


