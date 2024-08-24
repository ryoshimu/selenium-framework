import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, 'username')
        self.password_input = (By.ID, 'password')
        self.input = (By.ID, 'APjFqb')
        self.login_button = (By.ID, 'login')
        self.form()

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def form(self):
        print("入力")
        self.driver.find_element(*self.input).send_keys('aaaaa')
        time.sleep(1)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def login(self, username, password):
        # self.enter_username(username)
        # self.enter_password(password)
        # self.click_login()
        self.form()
