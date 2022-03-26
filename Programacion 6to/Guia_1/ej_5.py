print("Introduzca su palabra")

def isPalindrome(s):
    return s == s[::-1]

s=input()
ans = isPalindrome(s)

if ans:
    print("Es palindromo bro")
else:
    print("No es palindromo bro")

