# (1) 카운터와 누적변숙
cnt = tot =0
while cnt <5:
    cnt += 1   #cnt =cnt+1
    tot += cnt #tot = tot+cnt
    print(cnt, tot)

#1~100사이 3의 배수와 합과 원소 추출하기
cnt = tot =0
dataset =[]

while cnt <100:
    cnt +=1
    if cnt %3 ==0:
        tot +=cnt
        dataset.append(cnt)
print('1~100사이 3의 배수 합=%d' % tot)
print('dataset = ', dataset)

