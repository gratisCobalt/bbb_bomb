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
from logo import print_logo
import json
import os
from time import sleep

def init_listener():
    print_logo()
    print('Type \'help\' to get help')
    while (True):
        user_input = input('$ ')
        if (user_input == 'help'):
            print(
                '\'join\':   Join the conference.\n'
                '\'quit\':   Quit the program and bot.\n'
                '\'chat start\':   Start spamming the chat. (spam random stuff)\n'
                '\'chat stop\':   Stop spamming the chat. (spam random stuff)\n'
                '\'music play\':   Play a random .mp3 file in your music folder.\n'
                '\'music stop\':   Stop playing sounds\n'
                '\'mute\':   The bot will mute\n'
                '\'unmute\': The bot will unmute\n'
            )

        elif (user_input == 'join'):
            print('Joining the conference...')
            update_json('bot_join', True)

        elif (user_input == 'quit'):
            print('Stopping bot...')
            update_json('bot_quit', True)
            sleep(3)
            exit()

        elif (user_input == 'chat start'):
            print('Start chatting...')
            update_json('bot_chat', True)

        elif (user_input == 'chat stop'): # TODO
            print('Stop chatting...')
            update_json('bot_chat', False)

        elif (user_input == 'music play'):
            print('Playing audio...')
            update_json('bot_play_audio', True)

        elif (user_input == 'music stop'):
            print('Stopping audio...')
            update_json('bot_play_audio', False)

        elif (user_input == 'mute'):
            print('muting...')
            update_json('bot_muted', False)
            
        elif (user_input == 'unmute'):
            print('unmuting...')
            update_json('bot_muted', True)

        else:
            print('Unknown command!')
            print('Type \'help\' to get help')
        
def update_json(key, value):
    path_to_json = 'temp_config.json'
    with open(path_to_json, 'r') as jsonFile:
        data = json.load(jsonFile)

    data[key] = value

    with open(path_to_json, 'w') as jsonFile:
        json.dump(data, jsonFile)

init_listener()