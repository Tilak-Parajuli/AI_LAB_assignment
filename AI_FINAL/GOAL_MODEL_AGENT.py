import random
from time import sleep
from sys import exit
from random import randint 
def main(roomNum):
    status=[1,1,1];
    while(1):
        status[2]=random.randint(0,1)#current state
        if status[2]==0:
            goal(status,roomNum)
            print("Room ",roomNum,"is clean , Moving to Room:",anotherRoom(roomNum))
            roomNum=anotherRoom(roomNum)
            sleep(1)
        elif status[2]==1:
            print("Room ",roomNum,"is Dirty.\n CLEANING...")
            sleep(1)
        temp =status[1]
        status[1]=status[2]#previous states
        status[0]=temp #before previous
    
def anotherRoom(roomNum):
    if roomNum=='A' or roomNum=='a':
        return 'B'
    else:
        return 'A'
def goal(status,roomNum):
    if status[0]==0 and status[1]==0 and status[2]==0:
        print("Room: ",roomNum,"is clean")
        print("The room is clean from last checking. \n GOAL ACHIEVED.")
        print("\n\nGoing to sleep...")
        sleep(3)
        exit(0)

count=0
roomNum=input("Which room should I check first? (A/B) ")
main(roomNum)