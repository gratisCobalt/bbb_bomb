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
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import actions
from pygame._sdl2 import get_num_audio_devices, get_audio_device_name
from pygame import mixer
from time import sleep
import random
import json


class bomb():
    def __init__(self):
        print(
            "__          ______ ____        _                       ____  _                 _       ___       _         \n"
            "\ \        / /___ \___ \      | |                     |___ \| |               | |     / _ \     | |        \n"
            " \ \  /\  / /  __) |__) | __ _| |_ __ _ _ __ __ ___   ____) | | __ _ _ __   __| |_ __| | | | ___| | _____  \n"
            "  \ \/  \/ /  |__ <|__ < / _` | __/ _` | '__/ _` \ \ / /__ <| |/ _` | '_ \ / _` | '__| | | |/ __| |/ / __| \n"
            "   \  /\  /   ___) |__) | (_| | || (_| | | | (_| |\ V /___) | | (_| | | | | (_| | |  | |_| | (__|   <\__ \ \n"
            "    \/  \/   |____/____/ \__,_|\__\__, |_|  \__,_| \_/|____/|_|\__,_|_| |_|\__,_|_|   \___/ \___|_|\_\___/ \n"
            "                                   __/ |                                                                   \n"
            "                                  |___/                                                                    \n"
        )
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['--ignore-certificate-errors=yes', '--web-security=no', '--ssl-protocol=any'])
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()

    def run(self):
        with open('./Python/bomb/config.json') as f:
            data = f.read()
        obj = json.loads(data)
        audio_path = str(obj['audio_path'])
        site_url = str(obj['site_url'])
        audio_device_name = str(obj['audio_device_name'])
        usernames = str(obj['usernames'])
        play_audio_from_file = str(obj['play_audio_from_file'])

        self.driver.get(site_url)

        mixer.init()  # music player
        [get_audio_device_name(x, 0).decode()
         for x in range(get_num_audio_devices(0))]
        mixer.init(devicename=audio_device_name)
        mixer.music.load(audio_path)
        mixer.music.set_volume(0.1)
        mixer.music.play(loops=-1)  # infinite loop

        # check if step is alredy done
        join_name = True
        join = True
        audio = True
        audio_thumb = True
        join_with_audio = True

        while True:
            try:
                random_string = ''
                for _ in range(50):
                    random_integer = random.randint(97, 97 + 26 - 1)
                    flip_bit = random.randint(0, 1)
                    random_integer = random_integer - 32 if flip_bit == 1 else random_integer
                    random_string += (chr(random_integer))

                while (join_name):
                    join_input = self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div[2]/form/div/input[4]')  # name input
                    join_input.clear()
                    join_input.send_keys(random.choice(usernames))
                    join_name = False
                    break

                while (join):
                    self.driver.find_element_by_xpath('//*[@id="room-join"]').click() # join room button
                    join = False
                    break

                while (audio):
                    if (play_audio_from_file and join_with_audio):
                        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div/span/button[1]/span[1]/i').click()  # join with mic
                        join_with_audio = False
                        while (audio_thumb):
                            self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/span/button[1]/span[1]/i').click()  # thumbs up audiotest
                            audio_thumb = False
                            break
                    if (not play_audio_from_file and join_with_audio):
                        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div/span/button[2]/span[1]/i').click()  # join without mic
                        join_with_audio = False
                    audio = False
                    break

                text_send = self.driver.find_element_by_xpath('//*[@id="message-input"]')  # chat input
                text_send.clear()
                text_send.send_keys(random_string)

                self.driver.find_element_by_xpath('/html/body/div/main/section/div[4]/section/div/form/div[1]/button/span[1]/i').click()  # chat send button
            except Exception:
                pass


bomb().run()
