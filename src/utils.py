import time
import simpleaudio as sa

wave_obj = sa.WaveObject.from_wave_file("src/bell.wav")


def play_bell(wait=None):
    """
    Plays a bell sound. Optionally waits a few seconds.

    Args:
        wait (int, optional): Number of seconds to wait after starting playing the bell.
    """
    wave_obj.play()
    if wait:
        time.sleep(wait)


def start_timer(duration, extra_time=0):
    """
    Starts a countdown timer, optionally with extra time.

    Args:
        duration (int): The main duration of the timer in seconds.
        extra_time (int, optional): Additional time before the main duration starts, in seconds.
    """
    if extra_time:
        for remaining in range(extra_time, 0, -1):
            print(f"Temps restant: {duration + remaining}s ", end="\r")
            time.sleep(1)
        play_bell()
    for remaining in range(duration, 0, -1):
        print(f"Temps restant: {remaining}s ", end="\r")
        time.sleep(1)
    play_bell()
