zodiacs = ['쥐', '소', '범', '토끼', '용', '뱀', '말',
           '양', '원숭이', '닭', '개', '돼지']

year = int(input('출생연도: '))
year = (year-1900)%12

print('당신은 {}띠 입니다'.format(zodiacs[year]))
