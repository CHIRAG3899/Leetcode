#Given a list of unique words, return all the pairs of the distinct indices
#(i, j) in the given list, so that the concatenation of the two words words[i]
#+ words[j] is a palindrome.
#Example 1:
#Input: words = ["abcd","dcba","lls","s","sssll"]
#Output: [[0,1],[1,0],[3,2],[2,4]]
#Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
#Example 2:
#Input: words = ["bat","tab","cat"]
#Output: [[0,1],[1,0]]
#Explanation: The palindromes are ["battab","tabbat"]
#Example 3:
#Input: words = ["a",""]
#Output: [[0,1],[1,0]]

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        lookup={}
        for index,word in enumerate(words):
            lookup[word]=index
        
        def isPalindrome(word):
            for L in range(len(word)//2+1):
                if word[L]!=word[-L-1]:
                    return False
            return True
            
        ans=set()
        for index,word in enumerate(words):
            for L in range(len(word)):
                suffix=word[::-1][L:]
                if suffix in lookup and lookup[suffix] !=index:
                    if isPalindrome(word +suffix):
                        ans.add((index,lookup[suffix]))
                prefix=word[::-1][:L+1]
                if prefix in lookup and lookup[prefix] !=index:
                    if isPalindrome(prefix+word):
                        ans.add((lookup[prefix],index))
            
            if "" in lookup and word != "":
                if isPalindrome(word):
                    ans.add((lookup[""],index))
                    ans.add((index,lookup[""]))
        return list(sorted(ans))
