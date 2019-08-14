s = "Was it a cat I saw?"
s1 = "golog"
s2 = "gog"
s3 = "gg"
s4 = "g"
s5 = ""
s6= "sdfhk"
def is_palindrome(s):
	i = 0
	j = len(s) - 1

	while i < j:
		while (ord(s[i])<ord('A') or ord(s[i])>ord('z')) and i<j:
			i+=1
		while (ord(s[j])<ord('A') or ord(s[j])>ord('z')) and i<j:
			j-=1
		if s[i].lower() != s[j].lower():
			return False

		i+=1
		j-=1
	return True

print(is_palindrome(s))
print(is_palindrome(s1))
print(is_palindrome(s2))
print(is_palindrome(s3))
print(is_palindrome(s4))
print(is_palindrome(s5))
print(is_palindrome(s6))