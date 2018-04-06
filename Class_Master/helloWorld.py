print('Hello World')

def hello():
	print('Hello World')
	

def maximo(a,b,c):
	sol=-9999
	if a>b and a>c:
		sol=a
	elif b>c:
		sol=b
	else:
		sol=c
	return sol

def centenario(name,year):
	sol=''
	if isinstance(year,int):
		year=year+100
		sol= name + ' will reach 100 years in '+str(year)
	else:
		year=int(year)+100
		sol= name+ ' will reach 100 years in '+str(year)
	return sol

def wc(text):
	return len(text.split(' ')),len(text.split('\n')),len(text)

def rm(strring,i):
	if len(text)<i:
		print('WARNING')
	else:
	    return text[:i] + text[(i+1):]
	
def findTexto(path,word):
	f=open(path)
	return f.read().count(word)