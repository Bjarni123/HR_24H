import sys


def main():
    # Simple test script.
    sys.stderr.write("Input music, group, singer: ")
    music, group, singer = input().split(",")

    state_music_opinion(music, group, singer)
    print()
    state_music_opinion()

def state_music_opinion(genre = None, music_group = None, vocalist = None):
    if genre == None or len(genre) == 0:
        genre = "Classic Rock"
    if music_group == None or len(music_group) == 0:
        music_group = "The Beatles"
    if vocalist == None or len(vocalist) == 0:
        vocalist = "Freddie Mercury"

    print(f"The best type of music is {genre}.\nThe best music group is {music_group}.\nThe best lead vocalist is {vocalist}.")


# Definition for state_music_opinion goes here.


if __name__ == "__main__":
    main()