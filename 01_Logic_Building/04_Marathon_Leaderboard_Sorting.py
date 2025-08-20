import json


def sortMarathonResults(runners):
    # Your implementation here
    return sorted(runners, key=lambda x: (x["time"], x["name"]))


if __name__ == "__main__":
    runners = [
        {"name": "John", "time": 150},
        {"name": "Alice", "time": 120},
        {"name": "Bob", "time": 150},
    ]
    sorted_runners = sortMarathonResults(runners)
    print(json.dumps(sorted_runners))
