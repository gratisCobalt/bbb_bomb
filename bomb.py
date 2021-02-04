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
from time import sleep

from pygame import mixer
from pygame._sdl2 import get_audio_device_name, get_num_audio_devices
from selenium import webdriver
from selenium.webdriver.common import actions
from selenium.webdriver.common.keys import Keys
from logo import print_logo
import string

class bomb():

    random_string = ''
    audio_files = []

    # vars from config.json
    bot_join_now = False
    bot_quit_now = False
    bot_chat = False
    bot_play_audio = False
    bot_muted = True

    audio_path = ''
    site_url = ''
    audio_device_name = ''
    volume = 1
    greetings = []
    usernames = []

    # check if step is alredy done
    input_username = True
    join = True
    audio = False
    audio_thumb = False
    greeting = True
    update = True

    def run(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['--ignore-certificate-errors=yes', '--web-security=no', '--ssl-protocol=any'])
        options.add_argument("--disable-infobars")
        options.add_argument("start-maximized")
        options.add_experimental_option("prefs", {"profile.default_content_setting_values.media_stream_mic": 1})
        self.driver = webdriver.Chrome(options=options)

        b.read_json()
        self.driver.get(b.site_url)
        b. random_string = b.get_random_string()
        b.init_musicplayer()
        b.bot_chat = True

        while (True):
            if b.bot_join_now:
                b.join_room()
            if b.bot_quit_now:
                self.driver.quit()
                quit()
            if b.bot_play_audio:
                b.play_audio()
            if b.greeting:
                b.chat()
            if b.bot_chat:
                b.chat()
            if not b.bot_muted:
                b.unmute()
            if b.bot_muted:
                b.mute()

            b.read_json()
            sleep(1)

    def join_room(self):
        while (b.input_username):
            try:
                join_input = self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div[2]/form/div/input[4]')  # name input
                join_input.clear()
                join_input.send_keys(random.choice(b.usernames)) # choose random name from [usernames]
                b.input_username = False
                break
            except Exception:
                pass
        
        while (b.join):
            try:
                self.driver.find_element_by_xpath('//*[@id="room-join"]').click()  # join room button
                b.join = False
                b.audio = True
                break
            except Exception:
                pass
        
        while (b.audio):
            try: # accept joining with microphone
                self.driver.find_element_by_css_selector("body > div.portal--27FHYi > div > div > div.content--IVOUy > div > div > span > button:nth-child(1) > span.label--Z12LMR3").click()  # join with mic
                b.audio_thumb = True
            except Exception:
                pass

            while (b.audio_thumb): # accept "Yes, I do hear myself" (echo test)
                try:
                    self.driver.find_element_by_css_selector('body > div.portal--27FHYi > div > div > div.content--IVOUy > div > span > button:nth-child(1) > span.label--Z12LMR3').click()  # thumbs up audiotest
                    b.audio_thumb = False
                    b.audio = False
                    break
                except Exception:
                    pass
        b.bot_join_now = False

    def unmute(self):
        try:
            mute_btn = self.driver.find_element_by_xpath('/html/body/div/main/section/div[1]/section[2]/div/div[2]/span/button[1]/span[1]/i') # mute button
            if (not b.bot_muted and 'unmute' in mute_btn.get_attribute('class')):
                mute_btn.click()
        except Exception:
            pass

    def mute(self):
        try:
            mute_btn = self.driver.find_element_by_xpath('/html/body/div/main/section/div[1]/section[2]/div/div[2]/span/button[1]/span[1]/i') # mute button
            if (b.bot_muted and not 'unmute' in mute_btn.get_attribute('class')):
                mute_btn.click()
        except Exception:
            pass
    
    def chat(self):
        for i in range(1,10):
            try:
                text_send = self.driver.find_element_by_xpath('//*[@id="message-input"]')  # chat input
                text_send.clear()
                if (b.greeting):
                    text_send.send_keys(random.choice(b.greetings))
                    b.greeting = False
                else:
                    text_send.send_keys(b.random_string)
                self.driver.find_element_by_xpath('/html/body/div/main/section/div[4]/section/div/form/div[1]/button/span[1]/i').click()  # chat send button
                break
            except Exception:
                pass

    def play_audio(self): # play the .mp3
        if (b.bot_play_audio):
            if (not mixer.get_busy()): # check if sound is already playing
                sleep(1)
                mixer.music.play(loops=0)  # -1 infinity loop
            

    def get_random_string(self): # for chat messages
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(20))

    def init_musicplayer(self): # get musicplayer ready
        mixer.init()
        [get_audio_device_name(x, 0).decode() for x in range(get_num_audio_devices(0))]
        mixer.init(devicename=b.audio_device_name)
        mixer.music.load(random.choice(glob.glob(b.audio_path)))
        mixer.music.set_volume(b.volume)

    def read_json(self): # get values from config.json
        with open('temp_config.json') as f:
            data = f.read()
        obj = json.loads(data)

        # these will be updated every few seconds
        b.bot_join_now = bool(obj['bot_join'])
        b.bot_quit_now = bool(obj['bot_quit'])
        b.bot_chat = bool(obj['bot_chat'])
        b.bot_play_audio = bool(obj['bot_play_audio'])
        b.bot_muted = bool(obj['bot_muted'])

        if (b.update): # only get these vars once
            b.audio_path = str(obj['audio_path'])
            b.site_url = str(obj['site_url'])
            b.audio_device_name = str(obj['audio_device_name'])
            b.volume = int(obj['volume'])
            b.usernames = list(obj['usernames'])
            b.greetings = list(obj['greetings'])
            update = False

print_logo()
b = bomb()
b.run()
