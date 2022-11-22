import random

lotto_number = list(range(1,46))

lotto_number = random.sample(lotto_number,6)

print(lotto_number)

lotto=[]
i=0
while i<6:
    rand_num=random.randint(1,46)
    if rand_num not in lotto:
        lotto.append(rand_num)
        i += 1

    # if rand_num in lotto:
    #     continue
    #     pass
    # else:
    #     lotto.append((rand_num))
    #     i += 1
print(f'출력값: {lotto}')
