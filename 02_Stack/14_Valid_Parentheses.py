# please implement this function only
def isValidParentheses(s):
    stack = []
    for char in s:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack or stack.pop() != "(":
                return False
    return not stack


if __name__ == "__main__":
    test_cases = ["()", "()[]{}", "(]", "", "((()))", "())", "(()"]
    for test in test_cases:
        result = isValidParentheses(test)
        print(f"'{test}' -> {'true' if result else 'false'}")
