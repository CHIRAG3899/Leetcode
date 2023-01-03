##Given a pattern and a string s, find if s follows the same pattern.

##Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

##Example 1:

##Input: pattern = "abba", s = "dog cat cat dog"
##Output: true
##Example 2:

##Input: pattern = "abba", s = "dog cat cat fish"
##Output: false
##Example 3:

##Input: pattern = "aaaa", s = "dog cat cat dog"
##Output: false

class Solution:
    def wordPattern(self, p: str, s: str) -> bool:
        words, w_to_p = s.split(' '), dict()

        if len(p) != len(words): return False
        if len(set(p)) != len(set(words)): return False # for the case w = ['dog', 'cat'] and p = 'aa'

        for i in range(len(words)):
            if words[i] not in w_to_p: 
                w_to_p[words[i]] = p[i]
            elif w_to_p[words[i]] != p[i]: 
                return False

        return True
        
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        # dictionary approach 
        # Time complexity: O(n)
        # Space complexity: O(n)
        
        words = str.split(" ")
        if not len(words) == len(pattern):
            return False
        
        mapping = dict() # key is the pattern, value is the word
        
        for i in range(len(words)):
            if pattern[i] not in mapping:
                # values() is a set - fast membership testing - O(1) amortised search
                if words[i] not in mapping.values(): 
                    mapping[pattern[i]] = words[i]
                else:
                    return False
            else:
                if not mapping[pattern[i]] == words[i]:
                    return False
        return True

class Solution:
    def wordPattern(self,pattern: str, s: str) -> bool:
        # Split the string into a list of words
        words = s.split()
        
        # Check if the number of words in the string is equal to the number of letters in the pattern
        if len(words) != len(pattern):
            return False
        
        # Create two dictionaries to store the mappings between letters and words and between words and letters
        letter_mapping = {}
        word_mapping = {}
        
        # Iterate through the pattern and words simultaneously
        for letter, word in zip(pattern, words):
            # If the letter is not in the letter mapping, add it and map it to the word
            if letter not in letter_mapping:
                letter_mapping[letter] = word
            # If the letter is already in the letter mapping, check if it is mapped to the same word
            elif letter_mapping[letter] != word:
                return False
            
            # If the word is not in the word mapping, add it and map it to the letter
            if word not in word_mapping:
                word_mapping[word] = letter
            # If the word is already in the word mapping, check if it is mapped to the same letter
            elif word_mapping[word] != letter:
                return False
        
        return True
        
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
            arr = s.split()
            if len(arr) != len(pattern):
                return False
            
            for i in range(len(arr)):
                if pattern.find(pattern[i]) != arr.index(arr[i]):
                    return False
            return True