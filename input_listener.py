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
import logo
import json
import os
from time import sleep

def init_listener():
    print('Type \'help\' to get help')
    while (True):
        user_input = input('$ ')
        if (user_input == 'help'):
            print(
                '\'join\':   The bot will join the conference.\n'
                '\'stop\':   The program will stop.\n'
                '\'chat\':   The bot will start to chat. (spam random stuff)\n'
                '\'play\':   The bot will play a random file in your music folder.\n'
                # '\'mute\':   The bot will mute himself (NOT SUPPORTED!)\n'
                '\'unmute\': The bot will unmute himself\n'
            )

        elif (user_input == 'join'):
            print('Joining the conference...')
            update_json('bot_join_now', True)

        elif (user_input == 'stop'):
            print('Stopping bot...')
            update_json('bot_quit_now', True)
            sleep(3)
            exit()

        elif (user_input == 'chat'):
            print('Spamming the chat...')
            update_json('bot_chat', True)

        elif (user_input == 'stop chat'):
            print('Stopping spam...')
            update_json('bot_chat', False)

        elif (user_input == 'play'):
            print('Playing audio...')
            update_json('bot_play_audio', True)

        elif (user_input == 'mute'):
            print('muting...')
            update_json('bot_mute', False)
            
        elif (user_input == 'unmute'):
            print('unmuting...')
            update_json('bot_unmute', True)

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