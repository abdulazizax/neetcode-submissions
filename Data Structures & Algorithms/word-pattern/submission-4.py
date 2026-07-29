class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        
        if len(pattern) != len(words):
            return False

        charToWord = {}
        wordToChar = {}

        for ch, w in zip(pattern, words):
            if ch in charToWord and charToWord[ch] != w:
                return False
            if w in wordToChar and wordToChar[w] != ch:
                return False

            charToWord[ch] = w 
            wordToChar[w] = ch

        return True