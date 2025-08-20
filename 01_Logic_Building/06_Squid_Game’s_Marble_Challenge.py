def prefix_arr(lst):
    prefix_list = [0] * len(lst)
    prefix_list[0] = lst[0]
    for idx in range(1, len(lst)):
        prefix_list[idx] = prefix_list[idx - 1] + lst[idx]
    return prefix_list


def process_queries(n, marbles, queries):
    # Your code here
    # Step 1: build prefix sum
    prefix = prefix_arr(marbles)
    results = []
    # Step 2: answer each query
    for l, r in queries:
        if l == 1:
            results.append(prefix[r - 1])
        else:
            results.append(prefix[r - 1] - prefix[l - 2])
    return results


if __name__ == "__main__":
    n, q = 5, 3
    marbles = [1, 2, 3, 4, 5]
    queries = [[1, 3], [2, 5], [1, 5]]
    results = process_queries(n, marbles, queries)
    for res in results:
        print(res)
