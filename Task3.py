eng = { 1:'AEIOULNSTR',
      	2:'DG',
      	3:'BCMP',
      	4:'FHVWY',
      	5:'K',
      	8:'JZ',
      	10:'QZ'}
rus = { 1:'АВЕИНОРСТ',
      	2:'ДКЛМПУ',
      	3:'БГЁЬЯ',
      	4:'ЙЫ',
      	5:'ЖЗХЦЧ',
      	8:'ШЭЮ',
      	10:'ФЩЪ'}
n = abs(int(input('Введите 1, если слово на английском, либо 0, если в русском: ')))
word = input('Введите слово: ').upper()
if n == 1:
	t = sum([k for i in word for k, v in eng.items() if i in v])
	print('--->>', t)
elif n == 0:
	t1 = sum([k for i in word for k, v in rus.items() if i in v])
	print('--->>', t1)