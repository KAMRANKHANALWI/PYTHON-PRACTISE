# Smart Stream Quality Selector

## Problem Background

You are working at Dreamflix, a popular streaming service, on their adaptive streaming engine. Your task is to help the system automatically select the highest quality video that can be streamed without buffering, based on a user's available bandwidth.

Each video quality has a minimum bandwidth requirement, and the system must:

1. Select the highest quality that fits within the available bandwidth.
2. If no quality is suitable, return "No Quality Available".

This feature ensures smooth playback while maximizing video quality. Choosing the wrong quality may lead to either buffering (annoying) or unnecessarily low-quality playback.

## Problem Statement

You are working at Dreamflix, a popular streaming service, on their adaptive streaming engine. Your task is to help the system automatically select the highest quality video that can be streamed without buffering, based on a user's available bandwidth.

Each video quality has a minimum bandwidth requirement, and the system must:

1. Select the highest quality that fits within the available bandwidth.
2. If no quality is suitable, return "No Quality Available".

## Input Format

- An integer (b) representing the user's current bandwidth in kbps.
- An array (q) of (n) elements, where each element is a dictionary with the following keys:
  - **quality**: A string representing the quality of the stream.
  - **required**: An integer representing the minimum bandwidth required for that quality.

## Output Format

- A string representing the highest quality stream that won't buffer.
- If no quality is available, return "No Quality Available".

## Example

**Input:**

```
bandwidth = 5000 (kbps)
qualities = [
    {"quality": "4K", "required": 15000},
    {"quality": "1080p", "required": 5000},
    {"quality": "720p", "required": 3000},
    {"quality": "480p", "required": 1000}
]
```

**Output:**

```
1080p
```

**Explanation:**
The user's bandwidth is 5000 kbps, so the highest quality stream that won't buffer is "1080p".

## Constraints

- Bandwidth and required values are positive integers
- Quality names are non-empty strings
- At least one quality option is provided

## Approach

1. Iterate through all available qualities
2. Filter qualities that fit within available bandwidth
3. Among filtered qualities, select the one with highest bandwidth requirement
4. Return "No Quality Available" if no quality fits
5. Alternative: Sort qualities by requirement and use binary search for O(log n)
