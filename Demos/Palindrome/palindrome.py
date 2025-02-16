import re


def is_palindrome(s: str) -> bool:
    # use regex to remove all characters/spaces except letters and numbers, convert to lowercase
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

    # for the backwards word:
    return s == s [::-1]


