class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
        n = len(s)//2
        a = s[0:n]
        b = s[n:len(s)]
        v1 = 0
        v2 = 0
        for i in range(n):
            if a[i] in vowels:
                v1 += 1
            if b[i] in vowels:
                v2 += 1
        return v1 == v2
