import math

def check(tasks, max_instances, T):
    total_instance = 0
    for t in tasks:
        total_instance += math.ceil(t/T)
        if total_instance > max_instances:
            return False
    return True

def min_time_to_complete(tasks, max_instances):
    # Your code here
    low, high = 1, max(tasks)
    while low < high:
        mid = (low + high) // 2
        if check(tasks, max_instances, mid):
            high = mid   # feasible → maybe smaller
        else: 
            low = mid + 1   # not feasible → need more time
    
    return low

if __name__ == "__main__":
    test_cases = [
        ([2, 4, 8], 5),     # Expected: 4
        ([1, 1, 1], 3),     # Expected: 1
        ([10, 20, 30], 2),  # Expected: 30
        ([5], 1)            # Expected: 5
    ]
    
    for tasks, max_instances in test_cases:
        result = min_time_to_complete(tasks, max_instances)
        print(f"Tasks: {tasks}, max_instances={max_instances} -> {result}")