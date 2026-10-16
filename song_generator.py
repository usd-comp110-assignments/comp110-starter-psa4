"""COMP110 PSA4 (Song Generator)

Program to generate a song from a string of notes.

Author: <INSERT YOUR NAME AND EMAIL HERE>
"""

import sound

def scale_volume(original_sound, factor):
    """Decreases the volume of a sound object by a specified factor.

    DO NOT MODIFY THIS FUNCTION IN ANY WAY.

    Args:
        original_sound: The sound object whose volume is to be decreased.
        factor: The factor by which the volume is to be decreased.

    Returns:
        Sound: A new sound object that is a copy of original_sound, but with volumes
    scaled by factor.
    """
    scaled_sound = sound.copy(original_sound)

    for smpl in scaled_sound:
        # Scale left channel of smpl
        current_left = smpl.left
        scaled_left = round(current_left * factor)
        smpl.left = scaled_left

        # Scale right channel of smpl
        current_right = smpl.right
        scaled_right = round(current_right * factor)
        smpl.right = scaled_right

    return scaled_sound


def mix_sounds(snd1, snd2):
    """Mixes together two sounds (snd1 and snd2) into a single sound.
    
    If the sounds are of different length, the mixed sound will be the length
    of the longer sound.

    This returns a new sound: it does not modify either of the original
    sounds.

    Args:
        snd1: The first sound to mix
        snd2: The second sound to mix

    Returns:
        Sound: A Sound object that combines the two parameter sounds into a
    single, overlapping sound.
    """

    # Add your implementation here and then remove this comment.

    return None  # this is a placeholder. Remove this line.


def song_generator(notestring):
    """Generates a sound object containing a song specified by the notestring.

    Args:
        notestring: A string of musical notes and characters to
    change the volume and/or octave of the song.

    Returns:
        Sound: A song generated from the notestring given as a paramter.
    """

    # Add your implementation here and then remove this comment.

    return None  # this is a placeholder. Remove this line.


"""
Don't modify anything below this point.
"""

def main():
    """Asks the user for a notestring, generates the song from that notestring, then plays the resulting song."""
    print("Enter a notestring (without quotes):")
    ns = input()
    song = song_generator(ns)
    song.play()
    sound.wait_until_all_played()

if __name__ == "__main__":
    main()
