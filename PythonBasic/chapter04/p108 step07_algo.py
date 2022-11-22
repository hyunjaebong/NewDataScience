dateset = [5,10,18,22,35,55,75,103]
value=int(input("검색할 값 입력: "))

low=0
high=len(dateset) -1
loc=0
state=False

while (low <= high):
    mid=(low+high) //2

    if dateset[mid] >value:
        high = mid-1
    elif dateset[mid] < value:
        low = mid+1
    else:
        loc=mid
        state=True
        break

if state:
   print('찾는 위치: %d 번째' %(loc+1))
else:
   print('찾는 값은 없습니다.')