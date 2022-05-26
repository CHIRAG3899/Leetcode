#Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
#
#Note:
#
#Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
#In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3.
# 
#
#Example 1:
#
#Input: n = 00000000000000000000000000001011
#Output: 3
#Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
#Example 2:
#
#Input: n = 00000000000000000000000010000000
#Output: 1
#Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
#Example 3:
#
#Input: n = 11111111111111111111111111111101
#Output: 31
#Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.

class Solution:
    def hammingWeight(self, n: int) -> int:
        
        num_of_1s = 0
        
        for i in range(32):
            
            num_of_1s += (n & 1)
            
            n = n >> 1
            
        return num_of_1s
        
class Solution:
    def hammingWeight(self, n: int) -> int:
        
        counter = 0
    
        while n:
            
            # this will take out the right-most 1 of n    
            n = n & (n-1)
            
            # update counter
            counter += 1
        
        return counter
        
class Solution(object):
    def hammingWeight(self, n):
	
        mask_sum_2bit = 0x55555555
        mask_sum_4bit = 0x33333333
        mask_sum_8bit = 0x0F0F0F0F
        mask_sum_16bit = 0x00FF00FF
        mask_sum_32bit = 0x0000FFFF
        
        n = (n & mask_sum_2bit) + ((n >> 1) & mask_sum_2bit)
        n = (n & mask_sum_4bit) + ((n >> 2) & mask_sum_4bit)
        n = (n & mask_sum_8bit) + ((n >> 4) & mask_sum_8bit)
        n = (n & mask_sum_16bit) + ((n >> 8) & mask_sum_16bit)
        n = (n & mask_sum_32bit) + ((n >> 16) & mask_sum_32bit)
        
        return n