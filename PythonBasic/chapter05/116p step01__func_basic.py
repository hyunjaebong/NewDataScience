help(len)
dataset = list(range(1,6))
print(dataset)

print('len=', len(dataset))
print('sum=', sum(dataset))
print('max=', max(dataset))
print('min=', min(dataset))

import statistics
from statistics import  variance, stdev

print('평균:', statistics.mean(dataset))
print('중위수:', statistics.median(dataset))
print("표본 분산=", variance(dataset))
print("표본 표준편차=", stdev(dataset))
