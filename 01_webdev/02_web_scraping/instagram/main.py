import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InstagramBot:
    def __init__(self, username_, password_):

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=chrome_options)

        self.login_url = "https://www.instagram.com/accounts/login/?hl=en"

        self.username = username_
        self.password = password_

        self.followers = set()
        self.following = set()

    def login(self):

        self.driver.get(self.login_url)

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, 'username')))
        self.driver.find_element(By.NAME, 'username').send_keys(self.username)
        self.driver.find_element(By.NAME, 'password').send_keys(self.password)
        self.driver.find_element(By.XPATH, '//button[@type="submit"]').click()

        WebDriverWait(self.driver, 10).until(EC.url_to_be("https://www.instagram.com/accounts/onetap/?next=%2F&hl=en"))

    def scroll_to_bottom(self):

        time.sleep(5)

        for _ in range(43):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight",
                                       self.driver.find_element(By.CSS_SELECTOR, "div._aano"))
            time.sleep(3)

    def get_following(self):

        self.driver.get(f'https://www.instagram.com/{self.username}/following/?next=%2F&hl=en')

        self.scroll_to_bottom()

        # Locate the main container div
        main_container = self.driver.find_elements(By.CLASS_NAME, "x1dm5mii")

        for i in range(len(main_container)):
            insta_handle = main_container[i].find_element(By.CLASS_NAME, "_aacl").text
            self.following.add(insta_handle)

        print(len(self.following))
        print(self.following)

    def get_followers(self):

        self.driver.get(f'https://www.instagram.com/{self.username}/followers/?next=%2F&hl=en')

        self.scroll_to_bottom()

        # Locate the main container div
        main_container = self.driver.find_elements(By.CLASS_NAME, "x1dm5mii")

        for i in range(len(main_container)):
            insta_handle = main_container[i].find_element(By.CLASS_NAME, "_aacl").text
            self.followers.add(insta_handle)

        print(len(self.followers))
        print(self.followers)

    def you_follow_they_dont(self):
        not_following_back = self.following - self.followers
        print("You follow, but they don't follow back:")
        print(not_following_back)

    def they_follow_you_dont(self):
        not_followed_back = self.followers - self.following
        print("They follow, but you don't follow back:")
        print(not_followed_back)

    def close(self):
        self.driver.quit()

username = "YOUR_USER_NAME"
password = "YOUR_PASSWORD"

bot = InstagramBot(username, password)
bot.login()
bot.get_following()
bot.get_followers()
bot.you_follow_they_dont()
bot.they_follow_you_dont()
bot.close()
