b = 99 ;

#99 bottles of beer on the wall, 99 bottles of beer.
#Take one down and pass it around, 98 bottles of beer on the wall.//
#1 bottle of beer on the wall, 1 bottle of beer.
#Take one down and pass it around, no more bottles of beer on the wall.
#No more bottles of beer on the wall, no more bottles of beer. 
#Go to the store and buy some more, 99 bottles of beer on the wall.
while b >0  :
	if b==1:
		print str(b)+" bottle of beer on the wall, "+str(b)+" bottle of beer.";
	else:
		print str(b)+" bottles of beer on the wall, "+str(b)+" bottles of beer.Take one down and pass it around, "+str(b-1)+" bottles of beer on the wall"
	b=b-1;
print "Take one down and pass it around, no more bottles of beer on the wall. Go to the store and buy some more, 99 bottles of beer on the wall";