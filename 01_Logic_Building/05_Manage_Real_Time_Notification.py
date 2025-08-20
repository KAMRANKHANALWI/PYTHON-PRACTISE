import json


def count_notifications(notifications):
    # Implement your logic here
    # Step 1: Count notifications
    counts = {}
    for noti in notifications:
        if noti in counts:
            counts[noti] += 1
        else:
            counts[noti] = 1
    # Step 2: Convert dictionary into a list of object
    result = []
    for category, count in counts.items():
        result.append({"category": category, "count": count})
    # Step 3: Sort alphabetically by category name
    result = sorted(result, key=lambda x: x["category"])
    return result


if __name__ == "__main__":
    notifications = ["Event", "Offer", "Event", "Update", "Offer", "Offer", "Event"]
    result = count_notifications(notifications)
    print(json.dumps(result))
