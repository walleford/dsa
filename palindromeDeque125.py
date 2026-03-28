from collections import deque

def is_palindrome(s):
    d = deque(c.lower() for c in s if c.isalnum())
    if len(d) == 0:
        return True
    while len(d) > 1:
        left, right = d.popleft(), d.pop()
        if left != right:
            return False
    return True