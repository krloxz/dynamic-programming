import random
import string

import pytest


def longest_palindrome(string, head=0, tail=None):
  if (tail == None):
    tail = len(string) - 1

  if (is_palindrome(string, head, tail)):
    return string[head:tail + 1]

  return max_length_string(
    longest_palindrome(string, head, tail - 1),
    longest_palindrome(string, head + 1, tail)
  )


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


@pytest.mark.skip(reason="takes several seconds to complete")
def test_failure_on_recursion_limit():
  print(longest_palindrome("".join(random.sample(string.ascii_letters, 25))))
