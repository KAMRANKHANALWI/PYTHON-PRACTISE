def generate_parenthesis(n):
    result = []
    def backtrack(path, open_count, close_count):
        if open_count == close_count == n:
            result.append(path)
            return
        
        # option 1: add "(" if still available
        if open_count < n:
            backtrack(path + "(", open_count + 1, close_count)
            
        # option 2 : add ")" if valid
        if close_count < open_count:
            backtrack(path + ")", open_count, close_count + 1)
            
    backtrack("(", 1, 0)
    return result

print(generate_parenthesis(3))            