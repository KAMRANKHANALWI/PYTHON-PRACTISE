def is_palindrome(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def can_be_palindrome(s):
    # you need to implement this function only
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            # Option A: skip left, Option B: skip right
            return is_palindrome(s, left + 1, right) or is_palindrome(
                s, left, right - 1
            )
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    s = "racecar"
    result = can_be_palindrome(s)
    print("YES" if result else "NO")
