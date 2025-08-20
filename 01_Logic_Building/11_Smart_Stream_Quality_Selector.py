class Quality:
    def __init__(self, quality, required):
        self.quality = quality
        self.required = required


def select_stream_quality(bandwidth, qualities):
    # best = None
    # for q in qualities:
    #     if q.required <= bandwidth:
    #         best = q.quality
    # return best if best is not None else "No Quality Available"
    left, right = 0, len(qualities) - 1
    best = None

    while left <= right:
        mid = (left + right) // 2
        if qualities[mid].required <= bandwidth:
            # this quality fits, but maybe there's a better (higher) one
            best = qualities[mid].quality
            left = mid + 1
        else:
            # requirement too high, go left
            right = mid - 1
    return best if best is not None else "No Quality Available"


if __name__ == "__main__":
    qualities = [
        Quality("480p", 1000),
        Quality("720p", 3000),
        Quality("1080p", 5000),
        Quality("4K", 15000),
    ]
    bandwidth = 5000
    result = select_stream_quality(bandwidth, qualities)
    print(result)
