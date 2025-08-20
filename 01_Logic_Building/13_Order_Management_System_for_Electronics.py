def most_influential_user(influence_score):
    # you have to implement the most_influential_user() only
    max_score = -1
    max_user = -1
    for i in range(len(influence_score)):
        if influence_score[i] > max_score:
            max_score = influence_score[i]
            max_user = i
        elif influence_score[i] == max_score and i < max_user:
            max_user = i
    return max_user


if __name__ == "__main__":
    # Example: 6 users, edges: 1->2, 2->3, 3->4, 4->5
    n, m = 6, 4
    influence_score = [0] * n
    edges = [(1, 2), (2, 3), (3, 4), (4, 5)]

    for u, v in edges:
        if u != v:
            influence_score[v] += 1

    result = most_influential_user(influence_score)
    print(result)
