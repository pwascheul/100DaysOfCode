import os,sys
usr_ans = raw_input("you are going to delete the out.text file, please type y for deletion, no for cancel: ")
if usr_ans =='y':
	if  os.path.exists("out.text"): 
		os.remove("out.text")
	else:
		print ("sorry no such file")
else :
	print"sorry wrong entry ... exiting"
	sys.exit(0)