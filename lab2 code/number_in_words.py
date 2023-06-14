import re

exp_dict = {
	-1: ['копейка', 'копейки', 'копеек'],
	0: ['рубль', 'рубля', 'рублей'],
	1: ['тысяча', 'тысячи', 'тысяч'],
	2: ['миллион', 'миллиона', 'миллионов'],
	3: ['миллиард', 'миллиарда', 'миллиардов']
}

numerals_he = [
	'', 'один', 'два', 'три', 'четыре',
	'пять', 'шесть', 'семь', 'восемь', 'девять',
]

numerals_she = ['', 'одна', 'две']
for numerals in numerals_he[3:]:
	numerals_she.append(numerals)

ten_to_twenty = [
	'десять', 'одиннадцать', 'двенадцать',
	'тринадцать', 'четырнадцать', 'пятнадцать',
	'шестнадцать', 'семнадцать', 'восемнадцать',
	'девятнадцать'
]

tens = [
	'', '', 'двадцать', 'тридцать',
	'сорок', 'пятьдесят', 'шестьдесят',
	'семьдесят', 'восемьдесят', 'девяносто'
]

hundreds = [
	'', 'сто', 'двести', 'триста',
	'четыреста', 'пятьсот', 'шестьсот',
	'семьсот', 'восемьсот', 'девятьсот'
]

def add_numeral(num, exp):
	if abs(exp) == 1:
		return numerals_she[num % 10]
	return numerals_he[num % 10]

def simple_number_in_word(num, exp):
	if num == 0 and exp == -1:
		return '00 копеек'
	if num == 0 and exp > 0:
		return ''
	res = ''
	if num >= 100:
		res += hundreds[num // 100] + ' '
	if num >= 10:
		if (num // 10) % 10 == 1:
			res += ten_to_twenty[num % 10] + ' '
		else:
			res += tens[(num // 10) % 10] + ' '
			res += add_numeral(num, exp) + ' '
	else:
		res += add_numeral(num, exp) + ' '
	if num % 10 == 1:
		exp = exp_dict[exp][0]
	elif num % 10 in [2, 3, 4]:
		exp = exp_dict[exp][1]
	else:
		exp = exp_dict[exp][2]
	return res + exp

def number_in_words(num, exp=0):
	if num < 1000:
		return simple_number_in_word(num, exp)
	return number_in_words(num // 1000, exp + 1) + \
		   ' ' + simple_number_in_word(num % 1000, exp)

def number_to_words(num):
	ruble = int(num)
	penny = int((num * 100) % 100)
	words = number_in_words(ruble) + ' ' + number_in_words(penny, -1)
	words = re.sub(' +', ' ', words)
	return words.capitalize()
