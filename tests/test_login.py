import logging
from selenium import webdriver
from pages.login_page import LoginPage
import yaml

def load_config():
    with open('config/config.yaml') as config_file:
        config = yaml.safe_load(config_file)
    return config

def run():
    config = load_config()
    driver = webdriver.Chrome()

    try:
        driver.get(config['url'])
        login_page = LoginPage(driver)
        login_page.login(config['username'], config['password'])

        if "Dashboard" in driver.title:
            print("Login successful!")
        else:
            raise Exception("Login failed! Dashboard title not found.")

    except Exception as e:
        logging.error(f"Error during test_login: {str(e)}")
        raise e  # 再度例外を送出してmain.pyでキャッチ

    finally:
        driver.quit()

if __name__ == "__main__":
    run()
