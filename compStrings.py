'''
Created on 10/17/18
@author:   Luke McEvoy
Pledge:    I pledge my honor I have abided by the Stevens Honor System

CS115 - Hw 6
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

#used for numToBinary
def isOdd(n):
    if n % 2 == 0:
        return False
    return True

#helper function for compressing the 64 bits user input
def numToBinaryPadded(n):
    s = numToBinary(n)
    return ('0'*(COMPRESSED_BLOCK_SIZE - len(s))) + s

#turns string of binary numbers to a number in base 10
def binaryToNum(s):
    if len(s) == 0:
        return 0
    return (int(s[0]) * 2**(len(s)-1)) + binaryToNum(s[1:len(s)])

#takes base 10 number and changes it to binary string
def numToBinary(n):
    if n==0:
        return ''
    elif isOdd(n):
        return numToBinary(n//2) + '1'
    else:
        return numToBinary(n//2) + '0'

#helper function for compress
#determines 
def helperLen(s):
    if len(s) == 1:
        return 1
    if s[1] == s[0]:
        return 1 + helperLen(s[1:])
    return 1

#takes a binary string S of length 64 as input and returns another binary string as output
def compress(s):
    def compresshelp(s,b):
        if s=='':
            return ''
        if s[0] != chr(b + ord('0')):
            return numToBinaryPadded(0) + compresshelp(s, 1-b)
        prefix_Len = min(helperLen(s),MAX_RUN_LENGTH)
        return numToBinaryPadded(prefix_Len) + compresshelp(s[prefix_Len:],1-b)
    return compresshelp(s,0)

'''
Question #1
325 max bits 64 x 5 + 5
'''

#"inverts" or "undoes" the compressing
def uncompress(s):
    def uncompresshelp(s,b):
        if s== '':
            return ''
        n = binaryToNum(s[:COMPRESSED_BLOCK_SIZE])
        return chr(b + ord('0'))*n + uncompresshelp(s[COMPRESSED_BLOCK_SIZE:], 1-b)
    return uncompresshelp(s, 0)

# return the ratio of the compressed size to the original size
def compression(n):
    return len(compress(n))/len(n)

'''
Question #2 Test:
 I tested the binary string 31*0 + 1 and saw that its compression was
 31% of the original
 Next, I tested the binary string 31*0 and saw that its compression was
 16% of original
The more switches in variables, the higher the compression ratio.
'''

def test(s):
    if s == '':
        return ''
    else:
        return chr(s[0]) + test(s[1:])


'''
Question #3
Laicompress(s) could never make an algorithm that always outputs a shorter string
because of the fact if there were 32 '0's and 32 '1' oscillating between each
other, a string around 5 times the length of original would be returned as
the padded binary numbers are added to front of each binary # change.

Also the algorithm can not make a shorter string because to do this the padding
count would need to be lowered which would eliminate the possibility to
uncompress the compressed string which is a problem.
'''
 



