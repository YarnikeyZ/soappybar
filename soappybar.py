from tkinter import *
import configparser
from os.path import abspath as wd
from os import listdir
import simpleaudio as sa

def main():
    # loading config part
    config = configparser.ConfigParser()
    config.read(f'{wd("")}/soap_config.ini')

    # openning & configuring window part
    window = Tk()
    window.title(config['window']['title'])
    window.configure(bg=config['colors']['window_bg'])

    # buttons \w sounds part
    cxr = [0, 0] # column x row
    sounds = listdir(config['btns']['folder'])
    sounds.sort()
    for s in range(0, len(sounds)):
        btn = Button(master=window,
                     text=sounds[s].replace(".wav", ""),
                     command=lambda sound=sounds[s]: sa.WaveObject.from_wave_file(f"{config['btns']['folder']}/{sound}").play()
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

        # grid handeling
        cxr[0] += 1
        if cxr[0]//int(config['btns']['columns']) == 1:
            btn.grid(column=cxr[0], row=cxr[1])
            cxr = [0, cxr[1]+1]
        else:
            btn.grid(column=cxr[0], row=cxr[1])


    try:
        window.mainloop()
    except KeyboardInterrupt:
        exit()

if __name__ == "__main__":
    main()
