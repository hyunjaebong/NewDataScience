position = ['과장','부장','대리','사장','대리','과장']
uni_position = list(set(position))
print('중복되지 않는 직위:', uni_position)

position_cnt = {}
for p in position:
    position_cnt[p] = position_cnt.get(p,0) + 1
print('각 직위별 빈도수:', position_cnt)