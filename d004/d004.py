import urllib2
import sys

#Try to get the address from args, else get it from a prompt
try:
    address = sys.argv[1]
except IndexError:
    address = str(raw_input("Address: "))

#Attempt to connect to the website
try:
    xhtml = urllib2.urlopen(address)
except urllib2.HTTPError:
    print "Could not connect to %s and pull down data" % address
    sys.exit(1)
    
#Read data from site and get title
data = xhtml.read()
title = data.split("<title>")[1].split("</title>")[0] #Crufty hack to get title

if len(title) < 1:
    print "Couldnt get page title, using address instead"
    title = address #If somehow we didnt get the title, write the the address

#Write data into the local file
open(title + ".xhtml", 'w').write(data)
print "%s -> %s.xhtml" % (address, title)