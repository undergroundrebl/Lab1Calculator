again = True
modeSLT = True

def add(arg1,arg2):

	type_arg1 = str(type(arg1))
	type_arg2 = str(type(arg2))

	print("The first value is of type: " + type_arg1)
	print("The second value is of type: " + type_arg2)

	if( (type_arg1 == type_arg2) and (type_arg1 == "<type 'int'>") ):
		print arg1 + arg2 
	elif( (type_arg1 == type_arg2) and (type_arg1 == "<type 'decimal'>") ):
		print arg1 + arg2
	elif( (type_arg1 == type_arg2) and (type_arg1 == "<type 'str'>") ):
		print arg1 + arg2
	elif( (type_arg1 == type_arg2) and (type_arg1 == "<type 'tuples'>") ):
		print arg1 + arg2
	elif( (type_arg1 == type_arg2) and (type_arg1 == "<type 'list'>") ):
		print arg1 + arg2
	elif( (type_arg1 == type_arg2) and (type_arg1 == "<type 'bool'>") ):
		print in1 and in2
	else:
		print "ERROR: " +str(type(in1)) + " is not equal to " + str(type(in2)) + " or the type is not supported"
	 

def sub(arg1,arg2):

	type_arg1 = str(type(arg1))
	type_arg2 = str(type(arg2))

	print("The first value is of type: " + type_arg1)
	print("The second value is of type: " + type_arg2)

	if( (type_arg1 == type_arg2) and (type_arg1 == "<type 'int'>") ):
		print arg1 - arg2 
	elif( (type_arg1 == type_arg2) and (type_arg1 == "<type 'decimal'>") ):
		print arg1 - arg2
	else:
		print "ERROR: " +str(type(in1)) + " is not equal to " + str(type(in2)) + " or the type is not supported"

while(again):
	print ('/////////////////////////////////////////////////////////////////////////////////////')
	('/////////////////////////////////////////////////////////////////////////////////////////')
	print ('/////////////////////////////////////////////////////////////////////////////////////')
	('/////////////////////////////////////////////////////////////////////////////////////////')
	print ('/////////////////////////////////////////////////////////////////////////////////////')
	('/////////////////////////////////////////////////////////////////////////////////////////')

	print("This is a calculator that adds different types of data.")

	while(modeSLT):

		ad0sb = raw_input("addition (+) : subtraction (-) ")

		if ad0sb == "+" or ad0sb == "-":
			in1 = input("Enter the first value: ")
			in2 = input("Enter the second value: ")
			
			if ad0sb == "+":
				print add (in1,in2)
			if ad0sb == "-" :
 	 			print sub(in1,in2)
 	 		break;
		else :
			print("Not a valid calculator symbol");
			continue;
	
	again = input("Go again? Type 1 or greater for yes, 0 for no: ")
	if again <= 2:
		print("END")
		again = False 
		