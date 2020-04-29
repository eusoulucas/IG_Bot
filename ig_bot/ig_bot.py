from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import random


class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(
            executable_path=r"C:\Users\lucad\OneDrive\Desktop\geckodriver-v0.26.0-win64\geckodriver.exe")

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(3)

        campo_user = driver.find_element_by_xpath(
            "//input[@name = 'username']")
        campo_user.click()
        campo_user.clear()
        campo_user.send_keys(self.username)
        #
        campo_password = driver.find_element_by_xpath(
            "//input[@name='password']")
        campo_password.click()
        campo_password.clear()
        campo_password.send_keys(self.password)
        campo_password.send_keys(Keys.RETURN)

        time.sleep(5)
        self.comment_pics('iceland')

    @staticmethod
    def human_typing(frase, onde_digitar):
        for letra in frase:
            onde_digitar.send_keys(letra)
            time.sleep(random.randint(1, 5)/40)

    def comment_pics(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(5)

        for i in range(1, 3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)

        hrefs = driver.find_elements_by_tag_name("a")
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        [href for href in pic_hrefs if hashtag in href]
        print(str(pic_hrefs) + '\n')

        for pic_href in pic_hrefs:
            driver.get(pic_href)
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(2)
            try:
                comentarios = ['cool', 'nice', 'woow', 'very good','amazing', 'this is terrific', 'incredible']
                driver.find_element_by_class_name('Ypffh').click()
                campo_comment = driver.find_element_by_class_name('Ypffh')
                time.sleep(random.randint(2, 5))
                self.human_typing(random.choice(comentarios), campo_comment)
                time.sleep(random.randint(10, 20))
                driver.find_element_by_xpath('//button[contains(text(), "Publicar")]').click()
                time.sleep(3)
            except Exception as e:
                print(e)
                time.sleep(2)


lbot = InstagramBot("luscasedu", "Lucas109109")
lbot.login()
