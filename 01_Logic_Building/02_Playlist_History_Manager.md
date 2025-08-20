# Playlist History Manager

## Problem Background

You are building a playlist manager for a music app. Users can add songs to their playlist and undo their last action if they make a mistake. Your task is to implement this functionality using a stack.

The undo feature will allow users to remove the last song added to the playlist. The system does not need to support a redo feature for now, keeping the task simple.

## Problem Statement

Write a function to simulate the add song and undo last action functionality of a playlist manager. The function should process a series of actions and return the final state of the playlist.

The actions can be:

1. **"addSong('Song Name')"**: Add a song to the playlist.
2. **"undo()"**: Remove the most recently added song.

You need to process a list of these actions and return the final playlist.

## Input Format

- A list of strings, where each string represents an action.
- 1 ≤ number of actions ≤ 100.

## Output Format

- A list of strings, where each string represents a song in the playlist.

## Example

**Input:** `["addSong('Song 1')", "addSong('Song 2')", "undo()", "addSong('Song 3')"]`  
**Output:** `["Song 1", "Song 3"]`

## Explanation

- Action 1: Add "Song 1". Playlist: ["Song 1"].
- Action 2: Add "Song 2". Playlist: ["Song 1", "Song 2"].
- Action 3: Undo the last action (remove "Song 2"). Playlist: ["Song 1"].
- Action 4: Add "Song 3". Playlist: ["Song 1", "Song 3"].

## Constraints

1. 1 ≤ number of actions ≤ 100.
2. Actions will always be valid (e.g., undo() will only appear if there is at least one song to undo).

## Approach

1. Initialize an empty playlist (stack)
2. Process each action in order
3. For addSong actions, extract the song name and add to playlist
4. For undo actions, remove the last song from playlist
5. Return the final playlist state
