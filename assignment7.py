# Assignment: 7 + 8
# Date: March 27th, 2019
# Author: Ben Nichols

# Open file in read only mode
# Read entire file (for q in file:)
#   - When number is found grab the line
#   - Line should be assigned 3 variables: Question type, Question number, Question answer

def main():
    try:
        qFile = open("test.txt", 'r')
    except FileNotFoundError:
        print("Whoops! Looks like that file couldn't be found. Make sure test.txt exists in the same folder as the program!")

    number = 1
    question = []
    answer = []

    for q in qFile:
        l = q.split('\t')

        if l[0] == "B":
            print("Question ",number,": ",l[1]," (T/F): ", sep='', end='')
        else:
            print("Question ",number,": ",l[1],": ", sep='', end='')

        answer.append(input())
        question.append(l[2].rstrip('\n'))

        number=number+1

    correct = 0
    mark = 0
    qFile.close()
    print("\n")
    print("Question#","Given Answer","Correct Answer",sep='\t')
    for i in range(len(question)):
        print(i+1,answer[i],question[i],sep='\t\t')
        if(question[i].lower() == answer[i].lower()):
            correct = correct + 1

    print("\n")
    print("Total number of questions:",len(question))
    print("Number of correct answers:",correct)
    print("Total mark:",correct)
    
        


main()
