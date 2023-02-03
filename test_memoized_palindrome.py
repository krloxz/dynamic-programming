import sys

import pytest


def longest_palindrome(string, head=0, tail=None, palindromes=None):
  if (tail == None):
    tail = len(string) - 1
  if (palindromes == None):
    palindromes = [[None for _ in range(len(string))] for _ in range(len(string))]

  if (palindromes[head][tail] != None):
    return palindromes[head][tail]

  if (is_palindrome(string, head, tail)):
    palindromes[head][tail] = string[head:tail + 1]
    return palindromes[head][tail]

  palindromes[head][tail] = max_length_string(
    longest_palindrome(string, head, tail - 1, palindromes),
    longest_palindrome(string, head + 1, tail, palindromes)
  )
  return palindromes[head][tail]


def is_palindrome(string, head, tail):
  if (head >= tail):
    return True
  return string[head] == string[tail] and is_palindrome(string, head + 1, tail - 1)


def max_length_string(a, b):
  if (len(a) >= len(b)):
    return a
  return b


def test_one_letter_palindrome():
  assert "a" == longest_palindrome("a")


def test_non_palindromic_string():
  assert "x" == longest_palindrome("xyz")


def test_simple_palindrome():
  assert "saippuakivikauppias" == longest_palindrome("saippuakivikauppias")


def test_palindrome_in_large_text():
  long_text = "The Finnish word for “soapstone vendor” is supposedly the longest palindrome in everyday use: saippuakivikauppias. "\
              "(What do you mean you don't have a trusted soapstone vendor?)"
  assert "saippuakivikauppias" == longest_palindrome(long_text)


def test_failure_on_recursion_limit():
  with pytest.raises(RecursionError) as e:
    longest_palindrome(
        "".join("a" for _ in range(sys.getrecursionlimit() * 2)))
