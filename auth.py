import pickle

class Auth:
    def __init__(self,driver):
        self.driver = driver

    def save_cookies(self):
        with open('cookies.pkl', 'wb') as file:
            pickle.dump(self.driver.get_cookies(), file)

    def load_cookies(self):
        with open('cookies.pkl', 'rb') as file:
            cookies = pickle.load(file)
            for cookie in cookies:
                self.driver.add_cookie(cookie)