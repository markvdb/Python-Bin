def get_integer(message, default):
#get integer number - error check included
	try:
		f=input (message)
		st=type(f)
		if f==0:
			f=default
			return int(f)
		elif f==" ":
			f=default
			return int(f)
		else:
			return int(f)
	except:
		print("Wrong Input! Try again")
		return(get_integer(message, default))
        
def get_float(message, default):
#get float number - error check included
	try:
		f=input (message)
		st=type(f)
		if f==0:
			f=default
			return float(f) ##dodo
		elif f==" ":
			f=default
			return float(f)  ##dodo
		else:
			return float(f)
	except:
		print("Wrong Input! Try again")
		return(get_float(message, default))
		
def get_string(message):
#get string as user input
	string=input(message)
	return string
	
def write_file (file, description, var):
#write to file
	file.write ("\n")
	file.write (str(description))
	file.write ("\t")
	file.write (str(var))
	
def write_table13 (fn, v1, v2, v3, v4, v5,v6, v7, v8, v9, v10, v11, v12, v13):
	fn.write("\n")
	fn.write(v1)
	fn.write("\t")
	fn.write(v2)
	fn.write("\t")
	fn.write(v3)
	fn.write("\t")
	fn.write(v4)
	fn.write("\t")
	fn.write(v5)
	fn.write("\t")
	fn.write(v6)
	fn.write("\t")
	fn.write(v7)
	fn.write("\t")
	fn.write(v8)
	fn.write("\t")
	fn.write(v9)
	fn.write("\t")
	fn.write(v10)
	fn.write("\t")
	fn.write(v11)
	fn.write("\t")
	fn.write(v12)
	fn.write("\t")
	fn.write(v13)
	return 
	
def write_table5 (fn, v1, v2, v3, v4, v5):
	fn.write("\n")
	fn.write(v1)
	fn.write("\t")
	fn.write(v2)
	fn.write("\t")
	fn.write(v3)
	fn.write("\t")
	fn.write(v4)
	fn.write("\t")
	fn.write(v5)
	return
