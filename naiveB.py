import csv
from decimal import *
mylist=[]
dicta={}
dictb={}
prob_attra={}
prob_attrb={}
proba=0
probb=0
w_a=0
w_b=0
with open("out1.csv","rb") as file1:
	mylist=csv.reader(file1)
	takelist = list(mylist)

def iter_data(list1):
	classa=0
	classb=0
	t_a=0
	t_b=0
	#print list1
				#proba=0
				#robb=0
	for i in list1:
		templist = []
		if(i[-1]==" 2"):
			t_a+=1
		else:
			t_b+=1
		for j in i:
			#templist.append(j)
			#print j
			if (i[-1]==" 2"):
				classa+=1
				if(j.lower() not in dicta):
					dicta[j.lower()]=1
					templist.append(j.lower())
				else:
					dicta[j.lower()]+=1
			else:
				classb+=1
				if(j.lower() not in dictb):
					dictb[j.lower()]=1
					templist.append(j.lower())
				else:
					dictb[j.lower()]+=1
	#print dicta
	global w_a
	global w_b
	w_a=classa
	w_b=classb
	#print "  CLASS A ",classa
	#print "  CLASS B ",classb
	#print t_a
	#print t_b
	#print "----------------------------------------------------------------------------------------"
	#print dictb
	global proba
	global probb
	proba=calc_prob(t_a,t_b)
	probb=calc_prob(t_b,t_a)
	#print proba
	#print probb
	global prob_attra
	global prob_attrb
	for i in dicta.keys():
				prob_attra[i]=calc_prob1(dicta[i],classa)
	#print prob_attra
	for i in dictb.keys():
				prob_attrb[i]=calc_prob1(dictb[i],classb)
	#print prob_attrb
def test_prob(list1):
	pa=1
	pb=1
	acc=0
	#print len(prob_attra)
	for i in list1:
		pa=Decimal(1)
		pb=Decimal(1)
		for x in range(len(i)-1):
			#print "P A1 :",pa," P B1 :",pb
			if(i[x].lower() in dicta.keys()):
				pa*=Decimal(prob_attra[i[x].lower()])
			else:
				pa*=1/Decimal(w_a)
			if(i[x].lower() in dictb.keys()):
				pb*=Decimal(prob_attrb[i[x].lower()])
			else:
				pb*=1/Decimal(w_b)
			#print "P A :",pa," P B :",pb
		#print proba,probb
		pa*=Decimal(proba)
		pb*=Decimal(probb)
		#print "P A !!:",pa," P B !!:",pb
		if(pa.compare(pb)>0):
			if(i[len(i)-1]==" 2"):
				acc+=1
			else:
				#print "Guess ",2
				#print "P A :",pa," P B :",pb
				print i
		else:
			if(i[len(i)-1]!=" 2"):
				acc+=1
			else:
				#print pa,"   ",pb
				print i
	print "ACC ",acc
	print float(acc)/len(list1)


def calc_prob(a,b):
	return float(a)/(a+b)
def calc_prob1(a,b):
	return float(a)/b
bigattr=[]
attr=[]
for x in takelist:
	z=x[0].split(" ")
	z.append(x[1])
	attr.append(z)
	attr.append(x[1])
	bigattr.append(z)

	attr=[]
#print bigattr
iter_data(bigattr[0:1200])

test_prob(bigattr[1200:1500])
