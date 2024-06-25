import random as rd
import time as tm

def dice_animation():
    outcometime=.5 #outcome takes [outcometime] second.
    numbers=10 #how many numbers shown in [outcometime] second.
    
    #this part is for animation
    for i in range(0,numbers):
        num=rd.randint(1,6)
        print("Outcome: ",num,end="\r")
        tm.sleep(outcometime/numbers)     
    #main outcome value is in else part
    else:
        num=rd.randint(1,6)
        print("Outcome: ",num)
#menu shown only on first time.
def firstMenu():
    while True:
        print("[1]Roll Dice\n[0]Exit")
        userinput=input("Enter Your Choice: ")
        if checkWrongInput(userinput):
            print("Wrong Input")
        else:
            break
    return userinput
#menu shown after every roll
def menu():
    while True:
        print("[1]Roll Again\n[0]Exit")
        userinput=input("Enter your Choice: ")
        if checkWrongInput(userinput):
            print("Wrong Input")
        else:
            break
    return userinput

#checking the input is correct or not.
#without this function program my misbehave according to userinput
def checkWrongInput(st):
    if st=="0" or st=="1":
        return 0
    else:
        return 1
    
#menucall
choice=firstMenu()

while choice!="0":
    #dice Output call
    dice_animation()
    
    #menu call
    choice=menu()
    
#exit message
print("Thank You")
print("<PROGRAM STOPPED>")