import sys
import random

def print_help():
    print("Welcome to Magic 8 Ball!")
    print("This is modeled ofter the Magic 8 Ball game that you asked a question and shook the ball")
    print("and the answer would appear.")
    print("So, ask your question and wait for your answer to appear!")
    print("With the argument b, and the filename for bad, the responses will be mean.")
    print("With the argument g, and the filename for good, the responses will be nice.")
    print("With both arguments b and g, the responses will be randomly chosen from nice and mean.")
    print("With the argument h, this help will be printed.")
    return


def read_files(good, bad):
    list_of_items=[]
    if good != None:
        try:
            with open(good,'r') as f:
                for line in f:
                    list_of_items.append(line)

        except FileNotFoundError:
            print("Sorry but",good,"does not exist!")
            exit(1)

    if bad != None:
        try:
            with open(bad, 'r') as f:
                for line in f:
                    list_of_items.append(line)

        except FileNotFoundError:
            print("Sorry but", bad, "does not exist!")
            exit(1)

    return list_of_items


def get_arguments():
    num_arg = len(sys.argv)
    number = 1
    good = None
    bad = None
    while num_arg > number:
        if sys.argv[number][0:1] == "h" or sys.argv[number][0:1] == "H":
            return "HELP", None, None
        elif sys.argv[number][0:1] == "g" or sys.argv[number][0:1] == "G":
            good = sys.argv[number+1][0:]
            number = number+2
        elif sys.argv[number][0:1] == "b" or sys.argv[number][0:1] == "B":
            bad = sys.argv[number+1][0:]
            number = number+2
        else:
            print("Unexpected argument",sys.argv[number]," - please read help.")
            exit(1)
    return None, good, bad

def play_game(list_of_sayings):
    print("hit enter to quit!")
    question="0"
    while True:
        question=input("Enter your question: ")
        if question == "":
            break
        print("Our mystical 8 ball has come up with an answer to your question!")
        print("Your question:",question)
        print("Our answer is:",list_of_sayings[random.randint(0,len(list_of_sayings))])




help, good, bad = get_arguments()

#print("help is", help, "good is", good, "bad is", bad)

if help == "HELP":
    print_help()
    quit()

list_of_items = read_files(good, bad)
play_game(list_of_items)
#for item in list_of_items:
#    print(item)


