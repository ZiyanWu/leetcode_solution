''''
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.
Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
''''
class Solution(object):
    def in_one_row(self,word):
        first=['Q','W','E','R','T','Y','U','I','O','P']
        second=['A','S','D','F','G','H','J','K','L']
        third=['Z','X','C','V','B','N','M']
        if(word[0].upper() in first):
            for c in word:
                if c.upper() not in first:
                    return 0
        if(word[0].upper() in second):
            for c in word:
                if c.upper() not in second:
                    return 0   
        if(word[0].upper() in third):
            for c in word:
                if c.upper() not in third:
                    return 0 
        return 1                 
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        return filter(self.in_one_row,words)
        
