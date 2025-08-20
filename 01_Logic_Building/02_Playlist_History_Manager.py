import json


def playlist_manager(actions):
    playlist = []
    for action in actions:
        if action.startswith("addSong("):
            song = action.split("'")[1]
            playlist.append(song)
        elif action == "undo()":
            if playlist:
                playlist.pop()
    return playlist


if __name__ == "__main__":
    actions = ["addSong('Song 1')", "addSong('Song 2')", "undo()", "addSong('Song 3')"]
    result = playlist_manager(actions)
    print(json.dumps(result))
