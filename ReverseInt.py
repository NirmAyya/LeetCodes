'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x 
causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0
'''

class Solution:
    def reverse(self, x: int) -> int:
        #if given input is 0 return 0
        if(x==0):
            return 0
        #convert to string
        numStr=str(x)
        #iterate backwards through the string
        reverseStr=""
        for counter in range(len(numStr)-1,-1,-1):
            reverseStr+=numStr[counter]       
        if(reverseStr[0]=="0"):
            reverseStr=reverseStr[1:]
        if(reverseStr[len(reverseStr)-1]=="-"):
            reverseStr="-"+reverseStr[:len(reverseStr)-1]
        #convert the string of digits back into an int
        final=int(reverseStr)
        #based on how large the number is return either 0 or that number
        if(abs(final)>2147483647):
            return 0
        else:
            return final