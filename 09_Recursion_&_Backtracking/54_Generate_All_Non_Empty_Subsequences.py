def generate_subsequences(s):
    result = []

    def dfs(index, current):
        if index == len(s):
            if current:
                result.append(current)
            return

        # choice 1: include s[index]
        dfs(index + 1, current + s[index])

        # choice 2: exclude s[index]
        dfs(index + 1, current)

    dfs(0, "")
    return result


print(generate_subsequences("abc"))
