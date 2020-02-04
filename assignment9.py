# Assignment 9
# Author: Ben Nichols
# Date: April 3rd, 2019

def part1():
    try:
        courseFile = open("Course1.txt", "r")
    except FileNotFoundError:
        print("Whoops! The file Course1.txt doesn't exist!")
    else:
        dictionary = {}
        i = 1
        for line in courseFile:
            l = line.split(",")
            name = l[2].rstrip() + " " + l[1];
            dictionary[i] = name
            i = i + 1
        courseFile.close()
        
        ID = int(input("Enter a student ID to search for (0 to stop): "))
        print(" ")
        while ID != 0 :
            try:
                print("Student ID:",ID)
                print("Name:",dictionary[ID])
            except:
                print("Student with ID",ID,"could not be found!")
            finally:
                print(" ")
                ID = int(input("Enter a student ID to search for (0 to stop): "))
                print(" ")

def part2():
    try:
        courseFile = open("Course1.txt", "r")
    except FileNotFoundError:
        print("Whoops! The file Course1.txt doesn't exist!")
    else:
        set1 = set()
        for line in courseFile:
            l = line.split(",")
            name = l[2].rstrip() + " " + l[1];
            set1.add(name)
        courseFile.close()

    try:
        courseFile = open("Course2.txt", "r")
    except FileNotFoundError:
        print("Whoops! The file Course2.txt doesn't exist!")
    else:
        set2 = set()
        for line in courseFile:
            l = line.split(",")
            name = l[2].rstrip() + " " + l[1];
            set2.add(name)
        courseFile.close()

    print("Students in both classes:\n",set1.intersection(set2))
    print("Students only in class 1:\n",set1.difference(set2))
    print("Students only in class 2:\n",set2.difference(set1))


part1()
part2()
