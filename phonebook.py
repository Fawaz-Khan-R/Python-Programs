#This function checks whether the given name exists in the phonebook dictionary or not.
def lookup(name):
    if name in phonebook:
        return name +"="+phonebook[name]
    else:
        return "Not found"

#Main function of the program.
n = int(input())
phonebook={}
for a in range(n):
    data=input().split()
    phonebook[data[0]]=data[1]
while True:
    try:
        name = input()
    except EOFError:
        break
    print(lookup(name))

"""
Sample input
3
fawaz 99912222
hassan 11122222
divyanshu 12299933
fawaz
harry
bhuvan

Sample output
fawaz=99912222
Not found
Not found
"""