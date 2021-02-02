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
import json
import random
import warnings
from time import sleep

from pygame import mixer
from pygame._sdl2 import get_audio_device_name, get_num_audio_devices
from selenium import webdriver
from selenium.webdriver.common import actions
from selenium.webdriver.common.keys import Keys

import logo

class bomb():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['--ignore-certificate-errors=yes', '--web-security=no', '--ssl-protocol=any'])
        options.add_argument("--disable-infobars")
        options.add_argument("start-maximized")
        options.add_experimental_option("prefs", {"profile.default_content_setting_values.media_stream_mic": 1})
        self.driver = webdriver.Chrome(options=options)

    def run(self):
        with open('./Python/bomb/config.json') as f:
            data = f.read()
        obj = json.loads(data)
        audio_path = str(obj['audio_path'])
        site_url = str(obj['site_url'])
        audio_device_name = str(obj['audio_device_name'])
        play_audio_from_file = (obj['play_audio_from_file'])
        write_text_to_chat = (obj['write_text_to_chat'])
        volume = 1 # float(obj['volume'])
        usernames = list(obj['usernames'])

        self.driver.get(site_url)

        mixer.init()  # music player
        [get_audio_device_name(x, 0).decode() for x in range(get_num_audio_devices(0))]
        mixer.init(devicename=audio_device_name)
        mixer.music.load(audio_path)
        mixer.music.set_volume(volume)

        # check if step is alredy done
        join_name = True
        join = True
        audio = True
        audio_thumb = False
        join_with_audio = True
        muted = True

        random_string = ''
        
        if (play_audio_from_file):
                mixer.music.play(loops=-1)  # infinite loop

        while (True):
            for _ in range(50):
                random_integer = random.randint(97, 97 + 26 - 1)
                flip_bit = random.randint(0, 1)
                random_integer = random_integer - 32 if flip_bit == 1 else random_integer
                random_string += (chr(random_integer))

            while (join_name):
                try:
                    join_input = self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div[2]/form/div/input[4]')  # name input
                    join_input.clear()
                    join_input.send_keys(random.choice(usernames))
                    join_name = False
                    break
                except Exception:
                    pass

            while (join):
                try:
                    self.driver.find_element_by_xpath('//*[@id="room-join"]').click()  # join room button
                    join = False
                    break
                except Exception:
                    pass

            while (audio):
                if (play_audio_from_file and join_with_audio):
                    try:
                        self.driver.find_element_by_css_selector("body > div.portal--27FHYi > div > div > div.content--IVOUy > div > div > span > button:nth-child(1) > span.label--Z12LMR3").click()  # join with mic
                        join_with_audio = False
                        audio_thumb = True
                    except Exception:
                        pass
                    while (audio_thumb):
                        try:
                            self.driver.find_element_by_css_selector('body > div.portal--27FHYi > div > div > div.content--IVOUy > div > span > button:nth-child(1) > span.label--Z12LMR3').click()  # thumbs up audiotest
                            audio_thumb = False
                            audio = False
                            break
                        except Exception:
                            pass

            while (muted):
                try:
                    mute_btn = self.driver.find_element_by_xpath('/html/body/div/main/section/div[1]/section[2]/div/div[2]/span/button[1]/span[1]/i') # mute button
                    if ('unmute' in mute_btn.get_attribute('class')):
                        muted = False
                        break
                    else:
                        mute_btn.click()
                        muted = False
                        break
                except Exception:
                    pass

            if (write_text_to_chat):
                text_send = self.driver.find_element_by_xpath('//*[@id="message-input"]')  # chat input
                text_send.clear()
                text_send.send_keys(random_string)

                self.driver.find_element_by_xpath('/html/body/div/main/section/div[4]/section/div/form/div[1]/button/span[1]/i').click()  # chat send button

logo.print_logo()
bomb().run()
