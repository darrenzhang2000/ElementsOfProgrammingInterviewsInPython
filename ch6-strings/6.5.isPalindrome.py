'''
remove nonalphanumeric and test is the case insenstive string is a palindrome
'''

def isPalindrome(s):
    i, j = 0, len(s) - 1
    while i < j:
        if not s[i].isalnum():
            i += 1
        elif not s[j].isalnum():
            j -= 1
        else:
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
    return True


s = 'a.bcbA'
print(isPalindrome(s))