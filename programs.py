# Reverse a string using slicing
def reverseString(s):
    return s[::-1]

print(reverseString("for"))  # Output: "rof"


# Reverse a string by converting to list and reversing
def reverseStringList(s):
    s_list = list(s)
    s_list.reverse()
    return ''.join(s_list)

print(reverseStringList("faizan"))  # Output: "naziaf"


# Check if a string is palindrome by reversing with list
def checkPalindromeList(s):
    s_list = list(s)
    s_list.reverse()
    reversed_s = ''.join(s_list)
    return reversed_s == s

print(checkPalindromeList("madamsd"))  # Output: False


# Check if a string is palindrome using slicing
def checkPalindrome(s):
    return s == s[::-1]

print(checkPalindrome('madamqwf'))  # Output: False
print(checkPalindrome('madam'))     # Output: True
