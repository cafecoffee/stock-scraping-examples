from pandas import DataFrame

# DataFrame: 2차원 형태 자료구조
raw_data = {'col0': [1, 2, 3, 4],
            'col1': [11, 22, 33, 44],
            'col2': [111, 222, 333, 444]}

data = DataFrame(raw_data)

print(data)
print(data['col0'])
print(data['col1'])

# Series 타입으로 출력되는 것을 확인할 수 있음. 결론적으로 키를 통해 Series로 접근함
print(type(data['col0']))


daeshin = { 'open': [11650, 11100, 11200, 11100, 11000],
            'high': [11650, 11100, 11200, 11100, 11000],
            'low': [11650, 11100, 11200, 11100, 11000],
            'close': [11650, 11100, 11200, 11100, 11000]}

daeshin_day = DataFrame(daeshin)
print(daeshin_day)


# Column 선택
daeshin_day2 = DataFrame(daeshin, columns=['open', 'close'])
print(daeshin_day2)


# Index 추가. 그냥 접근하려고 하면 에러남. loc를 통해 생성한 Index를 통해 접근 가능함
date = ['18.03.01', '18.03.02', '18.03.03', '18.03.04', '18.03.05']
daeshin_day3 = DataFrame(daeshin, columns=['open', 'high', 'low'], index=date)

print(daeshin_day3)
print(daeshin_day3['18.03.02'])
# print(daeshin_day3.loc['18.03.02'])
