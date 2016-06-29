b = 99 ;

#using a while loop to publish the sentences. once b=1 we chenge the sentence as bottles move to bottle. Last sentence is out of the loop.
while b >0  :
	if b==1:
		print str(b)+" bottle of beer on the wall, "+str(b)+" bottle of beer.";
	else:
		print str(b)+" bottles of beer on the wall, "+str(b)+" bottles of beer.Take one down and pass it around, "+str(b-1)+" bottles of beer on the wall"
	b=b-1;
print "Take one down and pass it around, no more bottles of beer on the wall. Go to the store and buy some more, 99 bottles of beer on the wall";