class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = 0
        palindrome = ''

        if s==s[::-1]:
            return s

        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                current = s[i:j]
                if current == current[::-1]:
                    if answer<len(current):
                        answer = len(current)
                        palindrome = current
        
        return palindrome