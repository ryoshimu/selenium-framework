import logging
from pages.login_page import LoginPage
from config.config import *
from auth import Auth

def run(driver):
    # driver = webdriver.Chrome()
    try:
        driver.get(LOGIN['url'])
        auth = Auth(driver)
        auth.save_cookies()
        login_page = LoginPage(driver)
        # login_page.login(config['username'], config['password'])
        print("Running test_login...222222")
        if "Dashboard" in driver.title:
            print("Login successful!")
        else:
            raise Exception("Login failed! Dashboard title not found.")

    except Exception as e:
        logging.error(f"Error during test_login: {str(e)}")
        raise e  # 再度例外を送出してmain.pyでキャッチ

    finally:
        driver.quit()