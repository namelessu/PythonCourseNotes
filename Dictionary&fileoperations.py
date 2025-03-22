# import bitmath
# number=int(input("enter the number"))
# operation=str(input("enter the type of operation:set,clear,toggle"))
# k=int(input ("enter the nth bit"))
# if(operation=="set"):
	# print (bitmath.setBit(number,k))
# elif(operation=="clear"):
	# print (bitmath.clearBit(number,k))
# elif(operation=="toggle"):
	# print (bitmath.toggleBit(number ,k ))

# elif(operation=="get"):
	# print (bitmath.getBit(number ,k ))
########################################################################################################################################################
#Dictionary syntax:-
# d={"a":10,"b":20,"c":30,"d":[1,2,3,4]}

# for i in d :
	# print(d[i])
	
# if "a" in d :
	# print("it exists")
# else:
	# pass

# print(d.values())	


# d=dict(name="ahmed",age=22)
# print(d)
########################################################################################################################################################
# print('''|******************************|
# |To add a new empolyee press 1|
# |to print employee data press 2|
# |To delete empolyee press 3|
# |******************************|
	   # ''')
# i=1
# employees={'name':"ahmed",'id':'1','job':"programmer",'salary':"100$"}{'name':"mohammed",'id':'2','job':"engineer",'salary':"300$"}{'name':"mahmoud",'id':'3','job':"technician",'salary':"50$"}
# while(i>0):
	# x=int(input("enter your choice"))
	# if(x==1):
		# employee['name']=input("enter the name")
		# employee['job']=input("enter the job")
		# employee['id']=input("enter the id of the empolyee")
		# employee['salary']=input("enter the id of the empolyee")
	# elif(x==2):
		# employee['id']=input("enter the id of the empolyee")
		# print(employee[id])
########################################################################################################################################################
# f=open("mfile.txt","r")
# l1=int(f.readline())
# l2=int(f.readline())
# l3=int(f.readline())
# l4=int(f.readline())
# lst=[]
# x=[l1,l2,l3,l4]
# lst.append(x)
# print(x)
# f.close()
########################################################################################################################################################
# port=[]
# counter=0
# for i in range(8):
	# pin=input("please enter the bit " +str(counter) +"mode: ")
	# pin=pin.lower()
	# port.append(pin)
	# counter+=1
# porta=''
# counter=0
# for i in range(8):
	# if port[counter]=="input":
		# porta='0'+porta
	# else:
		# porta='1'+porta
# counter+=1
# porta=open("init.c","w")   #"a" for append
# porta.write('''
# void init_PORTA_DIR(void)
# {
# DDRA=Ob'''+str(porta)+''';'''+'''
# }
# ''')
########################################################################################################################################################
try:
	f=open("nfile.txt","r")
	f.read()
	f.close()
except:
	print("no such file")

	