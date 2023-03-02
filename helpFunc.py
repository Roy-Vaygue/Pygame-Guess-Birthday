from pygame import mixer

mixer.init()
########Help fonctions###########
def split_lines(text):
    """
    Splits a string containing newline characters into a list of strings, where
    each string corresponds to one line of the input string.
    """
    lines = text.split('\n')
    return [line.strip() for line in lines if line.strip()]

def play_sound(soundFile):
    #Set preferred volume
    mixer.music.set_volume(0.8)
    #Load audio file
    mixer.music.load(soundFile)
    #Play the music
    mixer.music.play()