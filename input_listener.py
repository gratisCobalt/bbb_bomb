"""
__          ______ ____        _                       ____  _                 _       ___       _
\ \        / /___ \___ \      | |                     |___ \| |               | |     / _ \     | |
 \ \  /\  / /  __) |__) | __ _| |_ __ _ _ __ __ ___   ____) | | __ _ _ __   __| |_ __| | | | ___| | _____
  \ \/  \/ /  |__ <|__ < / _` | __/ _` | '__/ _` \ \ / /__ <| |/ _` | '_ \ / _` | '__| | | |/ __| |/ / __|
   \  /\  /   ___) |__) | (_| | || (_| | | | (_| |\ V /___) | | (_| | | | | (_| | |  | |_| | (__|   <\__ \
    \/  \/   |____/____/ \__,_|\__\__, |_|  \__,_| \_/|____/|_|\__,_|_| |_|\__,_|_|   \___/ \___|_|\_\___/
                                   __/ |
                                  |___/
"""
from pynput import keyboard
import logo
import bomb as b

def on_press(key):
    if key == keyboard.Key.esc:
        return False  # stop listener

    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys

    if k in ['up', 'down', 'left', 'right']:  # keys of interest
        # self.keys.append(k)  # store it in global-like variable
        if (k == 'up'):
            print('UNMUTE')
            b.unmute()
        elif (k == 'down'):
            print('PLAY MUSIC')
            b.play_audio()
        elif (k == 'left'):
            print('CHAT')
            b.chat()
        elif (k == 'right'):
            print('EXIT BOT')
            b.exit_bot()

listener = keyboard.Listener(on_press=on_press)
listener.start()  # start to listen on a separate thread
listener.join()  # remove if main thread is polling self.keys
