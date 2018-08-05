from pandas import Series

# Series: 1차원 형태 자료구조
series = Series([92600, 92400, 92100, 94300, 92300])

print(series[0])
print(series[2])
print(series[3])


# Index 추가
series2 = Series([92600, 92400, 92100, 94300, 92300], index=['2016-02-19',
                                                             '2016-02-18',
                                                             '2016-02-16',
                                                             '2016-02-15',
                                                             '2016-02-16'])

for date in series2.index:
    print(date)

for price in series2.values:
    print(price)


# 덧셈, 뺄셈
mine = Series([10, 20, 30], index=['naver', 'sk', 'kt'])
friend = Series([10, 22, 11], index=['kt', 'sk', 'naver'])

print(mine + friend)
