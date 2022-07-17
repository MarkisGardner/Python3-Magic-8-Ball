import sys

def print_help():
    print("Welcome to Magic 8 Ball!")
    print(
        "This is modeled ofter the Magic 8 Ball game that you asked a question and shook the ball and the answer would appear.")
    print("So, ask your question and wait for your answer to appear!")
    print("With the argument b, and the filename for bad, the responses will be mean.")
    print("With the argument g, and the filename for good, the responses will be nice.")
    print("With both arguments b and g, the responses will be randomly chosen from nice and mean.")
    print("With the argument h, this help will be printed.")
    return
def get_arguments():
    num_arg=len(sys.argv)
    number=1
    good=None
    bad=None
    while (num_arg > number):
        if sys.argv[number][0:1] == "h" or sys.argv[number][0:1] == "H":
            return "HELP",None,None
        if sys.argv[number][0:1] == "g" or sys.argv[number][0:1] == "G":
            good=sys.argv[number+1][0:]
            number=number+2
        if sys.argv[number][0:1] == "b" or sys.argv[number][0:1] == "B":
            bad=sys.argv[number+1][0:]
            number=number+2
    return None,good,bad

help, good, bad = get_arguments()
print ("help is",help,"good is",good,"bad is",bad)

if help == "HELP":
    print_help()
#read_text_file=open(file,"r")
#read_text_file.readable()


#try:
#    with open(filename,'r') as f:
#        for line in f:

#except FileNotFoundError:
#    print("Sorry but",filename,"does not exist!")


