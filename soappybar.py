from tkinter import *
import configparser
from os.path import abspath as wd
from os import listdir
import simpleaudio
import platform

def preloadSounds(sounds) -> list:
    """
    Preloads every sound from given list
    """
    soundsLoaded = []
    for sound in sounds:
        soundName = sound.replace(".wav", "")
        soundData = simpleaudio.WaveObject.from_wave_file(f"{config['btns']['folder']}\\{sound}")
        soundsLoaded.append((soundName, soundData))
    return soundsLoaded

def addSoundButton(window, sound, cxr) -> list:
    """
    Adds a button with sound on a window with set position 
    """
    btn = Button(master=window,
                 text=sound[0],
                 command=lambda: sound[1].play()
    )

    btn.configure(width=int(config['btns']['geometry'].split('x')[0])*2,
                  height=int(config['btns']['geometry'].split('x')[1]),
                  activebackground=config['colors']['btn_abg'],
                  background=config['colors']['btn_bg'],
                  highlightbackground=config['colors']['btn_bd'],
                  foreground=config['colors']['btn_text'],
                  activeforeground=config['colors']['btn_atext'],
                  font=(config['font']['name'], int(config['font']['size']), config['font']['mode']),
    )

    cxr[0] += 1
    if cxr[0]//int(config['btns']['columns']) == 1:
        btn.grid(column=cxr[0], row=cxr[1])
        cxr = [0, cxr[1]+1]
    else:
        btn.grid(column=cxr[0], row=cxr[1])
    return cxr

def main():
    global config
    try:
        # Config reading
        pathSymbol = '/' if platform.system() == "Linux" else '\\'
        fullPath = __file__
        lastPathSymbol = fullPath.rfind(pathSymbol)

        config = configparser.ConfigParser()
        config.read(f'{fullPath[:lastPathSymbol-len(fullPath)+1]}config.ini')

        # Window setup
        window = Tk()
        window.title(config['window']['title'])
        window.configure(bg=config['colors']['window_bg'])

        # Getting and preloading of sounds
        sounds = listdir(config['btns']['folder'])
        sounds.sort()
        sounds = preloadSounds(sounds)

        # Putting every sound on corresponding button
        cxr = [0, 0]
        for sound in sounds:
            cxr = addSoundButton(window, sound, cxr)

        window.mainloop()
    except KeyboardInterrupt:
        exit()

if __name__ == "__main__":
    main()
