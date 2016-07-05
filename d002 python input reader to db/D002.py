#!/usr/bin/env python

import sys

class User:

    #Sets up variables for the class & prints banner
    def __init__(self):
        self.username = ""
        self.age = 0
        self.uid = 0
        
        #Print a quick set of instructions so people dont get lost 
        print "Please fill in the correct data or type exit to quit"
        
    #Checks to see if the user wants to quit
    def check_quit(self, uinput):
        if uinput== "exit":
            sys.exit(0)


    #Gets the users forum username
    def get_username(self):
        user_input = raw_input("Type your forum username: ")
    
        self.check_quit(user_input)
    
        #Check string is correct length
        if len(user_input) > 20:
            print "Usernames must be less than 20 characters long"
            self.get_username()
        elif len(user_input) < 1:
            print "Usernames must be at least 1 character long"
            self.get_username()
        else:
            #Use exception handling to detect if user is giving invalid data
            try:
                self.username = str(user_input)
            except:
                print "Username must be in string format"
                self.get_username()
           
    #Gets the users age     
    def get_age(self):
        user_input = raw_input("Type your age: ")

        self.check_quit(user_input)
        
        #Convert the output of range() to string so we can convert safely
        #to integer (with error handling) later on
        if user_input not in str(range(1, 999999)):
            print "Please enter a number between 1 and 999999"
            self.get_age()
        else:
            try:
                self.age = int(user_input)
            except:
                print "Please enter a number between 1 and 999999"
                self.get_age()
           
    #Gets the users forum user id     
    def get_uid(self):
        user_input = raw_input("Type your forum user id: ")

        self.check_quit(user_input)

        #Convert the output of range() to string so we can convert safely
        #to integer (with error handling) later on      
        if user_input not in str(range(1, 999999)):
            print "Please enter a number between 1 and 999999"
            self.get_uid()
        else:
            try:
                self.uid = int(user_input)
            except:
                print "Please enter a number between 1 and 999999"
                self.get_uid()
                
    #Shows the final string
    def show_string(self):
        print "You are %s, aged %s next year you will be %s, with user id %s, the next user is %s." % (
              self.username, self.age, self.age + 1, self.uid, self.uid + 1)

if __name__ == "__main__":
    usr = User()
    usr.get_username()
    usr.get_age()
    usr.get_uid()
    usr.show_string()