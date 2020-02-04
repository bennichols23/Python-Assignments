# Assignment 6
# Author: Ben Nichols

def main():
    user = 0
    while user != 4:
        user = int(input("Press 1 to create a new gradebook. \nPress 2 to search into an existing gradebook. \nPress 3 to add a student grade to an existing gradebook. \npress 4 to terminate the program. \n\nEnter here: "))
        if user == 1:
            create()
        elif user == 2:
            search()
        elif user == 3:
            add()
        elif user != 4:
            print("Whoops! You must choose a valid option!",user,"is not a valid option!")
    print("Terminating program")
    
def create():
    user = 0
    while user != 3:
        name = input("Enter the name of the new gradebook to be created: ")
        try:
            newBook = open(name, 'r')
        except FileNotFoundError:
            newBook = open(name, 'w')
            newBook.close()
            print("\nA gradebook with name",name,"has been created!\n")
            user = 3
        else:
            print("\nA gradebook with name",name,"already exists.\n")
            user = int(input("Press 1 to replace the file\nPress 2 to try a different name\nPress 3 to do nothing and return to menu\n\nEnter here: "))
            if user == 1:
                newBook = open(name, 'w')
                print("\nA gradebook with name",name,"has been created!")
                user = 3
            if user == 2:
                print("")
            if user == 3:
                print("")
            newBook.close()

def search():
    print("search")

def add():
    print("add")

main()
