class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [an.lower() for an in s if an.isalnum()]
        if len(s) & 1 == 1:
           front = "".join(s[:len(s)//2][::-1])
           back = "".join(s[len(s)//2+1:]) 
        else:
            front = "".join(s[:len(s)//2][::-1])
            back = "".join(s[len(s)//2:])
            
        if front == back:
            return True
        return False

s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
print(s.isPalindrome("A"))
print(s.isPalindrome(" "))