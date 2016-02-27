import csv
from decimal import *
mylist=[]
dicta={}
dictb={}
dictc={}
prob_attra={}
prob_attrb={}
prob_attrc={}
proba=0
probb=0
probc=0
w_a=0
w_b=0
w_c=0
with open("out1.csv","rb") as file1:
	mylist=csv.reader(file1)
	takelist = list(mylist)

def iter_data(list1):
	classa=0
	classb=0
	classc=0
	t_c=0
	t_a=0
	t_b=0
	#print list1
				#proba=0
				#robb=0
	for i in list1:
		templist = []
		if(i[-1]==" 1"):
			t_a+=1
		elif(i[-1]==" 2"):
			t_b+=1
		else:
			t_c+=1
		for j in i:
			#templist.append(j)
			#print j
			if (i[-1]==" 1"):
				classa+=1
				if(j.lower() not in dicta):
					dicta[j.lower()]=1
					templist.append(j.lower())
				else:
					dicta[j.lower()]+=1
			elif(i[-1]==" 2"):
				classb+=1
				if(j.lower() not in dictb):
					dictb[j.lower()]=1
					templist.append(j.lower())
				else:
					dictb[j.lower()]+=1
			elif(i[-1]==" 3"):
				classc+=1
				if(j.lower() not in dictc):
					dictc[j.lower()]=1
					templist.append(j.lower())
				else:
					dictc[j.lower()]+=1
	#print dicta
	global w_a
	global w_b
	global w_c
	w_a=classa
	w_b=classb
	w_c=classc
	print "  CLASS A ",classa
	print "  CLASS B ",classb
	print t_a
	print t_b
	#print "----------------------------------------------------------------------------------------"
	#print dictb
	global proba
	global probb
	global probc
	'''proba=calc_prob(t_a,t_b,t_c)
	probb=calc_prob(t_b,t_a,t_c)
	probc=calc_prob(t_c,t_a,t_b)'''
	proba=calc_prob(classa,classb,classc)
	probb=calc_prob(classb,classa,classc)
	probc=calc_prob(classc,classa,classb)
	print proba
	print probb
	print probc
	global prob_attra
	global prob_attrb
	global prob_attrc
	for i in dicta.keys():
				prob_attra[i]=calc_prob1(dicta[i],classa)
	#print prob_attra
	for i in dictb.keys():
				prob_attrb[i]=calc_prob1(dictb[i],classb)
	for i in dictc.keys():
				prob_attrc[i]=calc_prob1(dictc[i],classc)
	
	print prob_attrc
def test_prob(list1):
	pa=1
	pb=1
	pc=1
	acc=0
	#print len(prob_attra)
	for i in list1:
		pa=Decimal(1)
		pb=Decimal(1)
		pc=Decimal(1)
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
			if(i[x].lower() in dictc.keys()):
				pc*=Decimal(prob_attrc[i[x].lower()])
			else:
				pc*=1/Decimal(w_c)
			
			#print "P A :",pa," P B :",pb
		#print proba,probb
		pa*=Decimal(proba)
		pb*=Decimal(probb)
		pc*=Decimal(probc)
		#print "P A !!:",pa," P B !!:",pb
		if(pa.compare(pb)>0 and pa.compare(pc)>0):
			if(i[len(i)-1]==" 1"):
				acc+=1
			else:
				print "Guess ",1
				#print "P A :",pa," P B :",pb
				print i
		elif(pb.compare(pa)>0 and pb.compare(pc)>0):
			if(i[len(i)-1]==" 2"):
				acc+=1
			else:
				print "Guess ",2
				#print pa,"   ",pb
				print i
		elif(pc.compare(pa)>0 and pc.compare(pb)>0):
			if(i[len(i)-1]==" 3"):
				acc+=1
			else:
				print "  Guess ",3
				print i
	print "ACC ",acc
	print float(acc)/len(list1)


def calc_prob(a,b,c):
	return float(a)/(a+b+c)
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
