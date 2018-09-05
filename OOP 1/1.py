import datetime
import time
import os
import getpass

class Database:
    def __init__(self):
        self.users={"Sudarshan":["allo",[],[]]}
        self.isAdmin=False
        self.admin="Sudarshan"
        self.logged=False
        self.loggedUser=""
    
    def addUser(self):
        
        if(self.isAdmin):
            name=input('New username: ')
            password = getpass.getpass('Password:')
            self.users[name]=[password,[],[]]
        elif(self.logged):
            print('You are not authorised to add users.')
        else:
            print("Please log in as admin to add users.")
            
    def delUser(self):
        
        if(self.isAdmin):
            try:
                name=input('Username of the user to be deleted: ')
                if(name==self.admin):
                    print("Cannot delete the admin.")
                else:
                    del self.users[name]
                    print("User was deleted successfully.")
            except KeyError:
                print("Make sure the username is correct.")
        elif(self.logged):
            print("You are not authorised to delete users.")
        else:
            print("Please log in as admin to delete users.")
            
    def login(self,name,password):
        if(name in self.users and self.users[name][0]==password):
            print("Welcome ",name+".")
            ts = time.time()
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d at %H:%M:%S')
            self.users[name][1].append("User logged in on "+st+".")
            if(name==self.admin):
                self.isAdmin=True
            self.logged=True
            self.loggedUser=name
        elif(name not in self.users):
            print("User not found in the database.")
        else:
            print("Wrong password. Try again.")
    
    def addInfo(self,info):
        if(self.logged==True):
            self.users[self.loggedUser][2].append(info)
        else:
            print("Please log in first to add info.")
            
    def showInfo(self):
        if(self.logged==True):
            for i in self.users[self.loggedUser][2]:
                print(i)
        else:
            print("Please log in fist to view info.")
        
    def viewLog(self):
        if(self.logged==True):
            for i in self.users[self.loggedUser][1]:
                print(i)
        else:
            print("Please log in first to view log.")
    def showUsers(self):
        if(self.isAdmin):
            print(self.users)
        else:
            print("You are not authorised to view the user-list.")
    
    def logout(self):
        if(self.logged):
            ans=input("Are you sure you want to logout as "+ str(self.loggedUser)+"?(1-Yes,0-No)")
            if(ans=='1'):
                self.logged=False
                ts = time.time()
                st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d at %H:%M:%S')
                self.users[name][1].append("User logged out on "+st+".")
                self.loggedUser=''
                self.isAdmin=False
                print("You have been logged out successfully.")
            else:
                print("You haven't been logged out.")
        else:
            print("No user login!")

ans=''

data=Database()
while(ans.lower()!="q"):
    print("\n\t\tWelcome to Database Management")
    print("1.Login\n2.Add User\n3.View User-Info\n4.View User-Log\n5.Add User-Info\n6.Delete User\n7.Logout\n8.View Users.\nQ.Quit")
    ans=input("Enter your response: ")
    os.system('cls')
    if(ans=='1'):
        name=input("Username: ")
        pswd = getpass.getpass('Password:')
        data.login(name,pswd)
    if(ans=='2'):
        data.addUser()
    if(ans=='3'):
        data.showInfo()
    if(ans=='4'):
        data.viewLog()
    if(ans=='5'):
        info=input("Enter the information: ")
        data.addInfo(info)
    if(ans=='6'):
        data.delUser()
    if(ans=='7'):
        data.logout()
    if(ans=='8'):
        data.showUsers()