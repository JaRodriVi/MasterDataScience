print('Clase Master 06v7')

def by2(x):
	return 2*x

def lby2(x):
	by2_b= lambda y: y*2
	return by2_b(x)

def callme(f,x):
	return f(x)

def ex3_1(l):
	square= lambda x: x*x
	return list(map(square,l))

def isVocal(s):
	vocals="aeiou"
	k=''
	for i in s:
		if i in vocals:
			k+=i.upper()
		else:
			k+=i.lower()
	return k

def ex3_2(l):
	return list(map(isVocal,l))

def isVocals_2(s):
	return ''.join(list(map(lambda x: x.upper() if x in "aeiouAEIOU" else x.lower(),s)))

def ex3_2_2(l):
	return list(map(isVocals_2,l))

def ex3_3(l,c):
	return list(filter(lambda x: not(c in x),l,c))

def ex5_2(l):
	return sorted(l,key=lambda x:len(set(x.lower())),reverse=True)

