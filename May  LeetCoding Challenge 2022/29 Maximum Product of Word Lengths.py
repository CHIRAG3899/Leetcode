#Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. If no such two words exist, return 0.
#
# 
#
#Example 1:
#
#Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
#Output: 16
#Explanation: The two words can be "abcw", "xtfn".
#Example 2:
#
#Input: words = ["a","ab","abc","d","cd","bcd","abcd"]
#Output: 4
#Explanation: The two words can be "ab", "cd".
#Example 3:
#
#Input: words = ["a","aa","aaa","aaaa"]
#Output: 0
#Explanation: No such pair of words.

class Solution:
    def maxProduct(self, words):
        d, ans = defaultdict(int), 0
        for word in words:
            for l in word:
                d[word] |= 1<<(ord(l) - 97)
                
        for w1, w2 in combinations(d.keys(), 2):
            if d[w1] & d[w2] == 0: 
                ans = max(ans, len(w1)*len(w2))
                
        return ans
        
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n=len(words)                        
        char_set = [set(words[i]) for i in range(n)] # precompute hashset for each word                                                  
        max_val = 0
        for i in range(n):
            for j in range(i+1, n):
                if not (char_set[i] & char_set[j]): # if nothing common
                    max_val=max(max_val, len(words[i]) * len(words[j]))
        
        return max_val   
        
