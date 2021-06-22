#Given a string s and an array of strings words, return the number of words[i]
#that is a subsequence of s.
#A subsequence of a string is a new string generated from the original string
#with some characters (can be none) deleted without changing the relative order
#of the remaining characters.
#For example, "ace" is a subsequence of "abcde".
# Example 1:
#Input: s = "abcde", words = ["a","bb","acd","ace"]
#Output: 3
#Explanation: There are three strings in words that are a subsequence of s: "a",
#"acd", "ace".
#Example 2:
#Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
#Output: 2

class Solution:
    def numMatchingSubseq(self, S, words):
        def isSubseq(word):
            curr = 0
            for symbol in word:
                ind = bisect_left(places[symbol], curr)
                if ind >= len(places[symbol]):
                    return False
                curr = places[symbol][ind] + 1
            
            return True
        
        places = defaultdict(list)
        for i, symbol in enumerate(S):
            places[symbol].append(i)
        
        return sum(isSubseq(word) for word in words)
