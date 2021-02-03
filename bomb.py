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
import glob
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

    random_string = ''
    audio_files = []

    # vars from json
    audio_path = ''
    site_url = ''
    audio_device_name = ''
    play_audio_from_file = False
    write_text_to_chat = False
    volume = 0
    usernames = []

    # check if step is alredy done
    join_name = True
    join = True
    audio = True
    audio_thumb = False
    muted = True

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['--ignore-certificate-errors=yes', '--web-security=no', '--ssl-protocol=any'])
        options.add_argument("--disable-infobars")
        options.add_argument("start-maximized")
        options.add_experimental_option("prefs", {"profile.default_content_setting_values.media_stream_mic": 1})
        self.driver = webdriver.Chrome(options=options)

    def run(self):
        b.read_json()
        self.driver.get(b.site_url)
        b.random_string = b.get_random_string()
        b.init_musicplayer()
        
        while (True):
            b.join_room()
            b.accept_audio()
            b.unmute()
            b.chat()

    def read_json(self):
        with open('./config.json') as f:
            data = f.read()
        obj = json.loads(data)

        b.audio_path = str(obj['audio_path'])
        b.site_url = str(obj['site_url'])
        b.audio_device_name = str(obj['audio_device_name'])
        b.play_audio_from_file = (obj['play_audio_from_file'])
        b.write_text_to_chat = (obj['write_text_to_chat'])
        b.volume = int(obj['volume'])
        b.usernames = list(obj['usernames'])

    def get_random_string(self):
        for _ in range(50):
            random_integer = random.randint(97, 97 + 26 - 1)
            flip_bit = random.randint(0, 1)
            random_integer = random_integer - 32 if flip_bit == 1 else random_integer
            b.random_string += (chr(random_integer))

    def join_room(self):
        while (b.join_name):
            try:
                join_input = self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div[2]/form/div/input[4]')  # name input
                join_input.clear()
                join_input.send_keys(random.choice(b.usernames))
                b.join_name = False
                break
            except Exception:
                pass
        
        while (b.join):
            try:
                self.driver.find_element_by_xpath('//*[@id="room-join"]').click()  # join room button
                b.join = False
                break
            except Exception:
                pass

    def init_musicplayer(self):
        mixer.init()  # music player
        [get_audio_device_name(x, 0).decode() for x in range(get_num_audio_devices(0))]
        mixer.init(devicename=b.audio_device_name)
        mixer.music.load(random.choice(glob.glob(b.audio_path)))
        mixer.music.set_volume(b.volume)

        if (b.play_audio_from_file):
            mixer.music.play(loops=-1)  # infinite loop

    def accept_audio(self):
        while (b.audio):
            try:
                self.driver.find_element_by_css_selector("body > div.portal--27FHYi > div > div > div.content--IVOUy > div > div > span > button:nth-child(1) > span.label--Z12LMR3").click()  # join with mic
                b.audio_thumb = True
            except Exception:
                pass

            while (b.audio_thumb):
                try:
                    self.driver.find_element_by_css_selector('body > div.portal--27FHYi > div > div > div.content--IVOUy > div > span > button:nth-child(1) > span.label--Z12LMR3').click()  # thumbs up audiotest
                    b.audio_thumb = False
                    b.audio = False
                    break
                except Exception:
                    pass

    def unmute(self):
        while (b.muted):
            try:
                mute_btn = self.driver.find_element_by_xpath('/html/body/div/main/section/div[1]/section[2]/div/div[2]/span/button[1]/span[1]/i') # mute button
                if ('unmute' in mute_btn.get_attribute('class')):
                    b.muted = False
                    break
                else:
                    mute_btn.click()
                    b.muted = False
                    break
            except Exception:
                pass

    def chat(self):
        if (b.write_text_to_chat):
            text_send = self.driver.find_element_by_xpath('//*[@id="message-input"]')  # chat input
            text_send.clear()
            text_send.send_keys(random_string)
            self.driver.find_element_by_xpath('/html/body/div/main/section/div[4]/section/div/form/div[1]/button/span[1]/i').click()  # chat send button

logo.print_logo()
b = bomb()
b.run()
