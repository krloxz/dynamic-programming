def longestPalindromeAt(string, index):
  if (len(string) - index == 1)
    return 1
  return max(
    longestPalindromeBetween(string, index, len(string) - 1),
    longestPalindromeAt(string, index + 1)
  )

def longestPalindromeBetween(string, head, tail):
  if (isPalindrome(string, head, tail))
    return tail - head
  return longestPalindromeBetween(string, head, tail - 1)

def isPalindrome(string, head, tail):
  if (head == tail)
    return true
  return
    string[head] == string[tail]
      && isPalindrome(string, head + 1, tail - 1)