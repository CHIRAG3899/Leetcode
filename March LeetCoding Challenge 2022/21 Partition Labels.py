#You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.
#Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.
#Return a list of integers representing the size of these parts.
#Example 1:
#Input: s = "ababcbacadefegdehijhklij"
#Output: [9,7,8]
#Explanation:
#The partition is "ababcbaca", "defegde", "hijhklij".
#This is a partition so that each letter appears in at most one part.
#A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
#Example 2:
#Input: s = "eccbbbbdec"
#Output: [10]


class Solution(object):
    def partitionLabels(self, S):
        last = {c: i for i, c in enumerate(S)}
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1
            
        return ans
        
        
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hsh = {}
        # generate indices for each character in the s
        for i,char in enumerate(s):
            if char in hsh:
                hsh[char].append(i)
            else:
                hsh[char] = [i]
    
        out = []
        left,right = None,None
        # maintain a left right index to know the range of char under one partition
        for key in hsh:
            # initialize it for the first keys first occurence and last occurence.
            if left is None:
                left = hsh[key][0]
                right = hsh[key][-1]
            # if the current keys indices are bigger than right, we have reached a point where our left and right can be paritioned separately.
            # hence add the length to the output and update left, right to current key index
            elif hsh[key][0]>right:
                out.append(right-left+1)
                left = hsh[key][0]
                right = hsh[key][-1]
            
            # else, update the right to the max index between right and last occurence of the current key
            else:
                right = max(right,hsh[key][-1])
        # finally add the last partition
        out.append(right-left+1)
        return out
        
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
		# base case if we only have 1 letter 
        if len(s)<2:
            return [1] #change to [len(s)]
        response = [] # final response
        memory = []  #track
        memory.append(s[0])# we already known that we have at least 2 letters
        count = 1 # counter 
        i = 1
        while i<len(s):
            if s[i] in memory:
                count+=1 #if the current value char is in our memory add the count
            else: # is a new character
                bl = False # boolean flag, true to add the new character into the current count or in a new
                for each in memory: #we want to keep track of each letter into the remaining string
                    if each  in s[i+1:]: #if at least one of the letters in our memory appers later, we can change the flag and stop the for 
                        bl = True
                        break
                if bl: # add the new letter into the memory
                    memory.append(s[i])
                    count+=1
                else:
                    memory = [] # empty the memory
                    memory.append(s[i]) # add the current new character 
                    response.append(count) # add the current count into the response
                    count = 1 #counter
            i+=1
        response.append(count) #add the remaining letters 
        return response