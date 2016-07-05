import os.path, sys 
if not os.path.exists("bhaarat.text"):  
    print "bhaarat.text is not available. Make sure it is in the working directory." 
    sys.exit() 
i,temp,langs,a=0,"",[],1 
bhaarat=open("bhaarat.text","r").readlines() #put bhaarat.text into a list with entries by line 
while i<22: 
    temp=bhaarat[i].lstrip("1234567890. ") #take the line in the current iteration and strip the numbering 
    if temp.startswith("H") or temp.startswith("S"):  
        langs.append("%s. %s" % (a,temp)) 
        a=a+1 
    i=i+1 
open("out.text","w").writelines(langs) #output the list of H and S languages to out.text 
open("bhaarat.text","a").write("23. English\n")