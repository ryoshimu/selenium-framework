import logging
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
import yaml

def load_config():
    with open('config/config.yaml') as config_file:
        config = yaml.safe_load(config_file)
    return config

def run():
    config = load_config()
    driver = webdriver.Chrome(ChromeDriverManager().install())

    try:
        driver.get(config['url'])
        login_page = LoginPage(driver)
        login_page.login(config['username'], config['password'])

        logout_button = driver.find_element_by_id('logout')
        logout_button.click()

        if "Login" in driver.title:
            print("Logout successful!")
        else:
            raise Exception("Logout failed! Login title not found.")

    except Exception as e:
        logging.error(f"Error during test_logout: {str(e)}")
        raise e  # 再度例外を送出してmain.pyでキャッチ

    finally:
        driver.quit()

if __name__ == "__main__":
    run()
