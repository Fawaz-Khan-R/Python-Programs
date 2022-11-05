#This whole program put together counts the number of 1's in the binary form of a base 10 decimal.

#This part of the program converts a base 10 decimal to binary.
def binary(dcm):
    if dcm == 0:
        return 0
    else:
        return dcm % 2 + 10 * binary(int(dcm / 2))

#This part of the program counts the number of 1's in any number.
def ones(num):
    string = str(num)
    one = 0
    mx = 0
    for i in range(len(string)):
        if string[i] == '1':
            one += 1
            if one > mx:
                mx = one
        if string[i] == '0':
            one = 0
    return mx
#Main program which uses the called functions.
if __name__ == '__main__':
    n = int(input().strip())
    
    m = binary(n)
    print(ones(m))
