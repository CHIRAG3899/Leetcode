##We define the usage of capitals in a word to be right when one of the following cases holds:

##All letters in this word are capitals, like "USA".
##All letters in this word are not capitals, like "leetcode".
##Only the first letter in this word is capital, like "Google".
##Given a string word, return true if the usage of capitals in it is right.

##Example 1:

##Input: word = "USA"
##Output: true
##Example 2:

##Input: word = "FlaG"
##Output: false

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        return (word == word.capitalize() or 
                word == word.upper()      or 
                word == word.lower()        )
                
                
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper() or word.islower() or word.title() == word:
            return True
        else:
            return False
            
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        for i in range(len(word) - 1):
            is_curr = 'A' <= word[i] <= 'Z'
            is_next = 'A' <= word[i + 1] <= 'Z'

            if (not is_curr and is_next) or (i and (is_curr and not is_next)):
                return False

        return True