def getTotalPage(m,n):
    totalPage = 0
    if m % n != 0:
        totalPage = m // n
        totalPage += 1
    else:
        totalPage = m // n

    return totalPage

print(getTotalPage(5, 10)) # 1 출력
print(getTotalPage(15, 10)) # 2 출력
print(getTotalPage(25, 10)) # 3 출력
print(getTotalPage(30, 10)) # 3 출력