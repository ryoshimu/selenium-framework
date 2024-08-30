import sys
import logging
from selenium import webdriver
from Util.ClassGenerator import ClassGenerator
from import_file.test_case import *

class Main:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
        self.driver = webdriver.Chrome(options=chrome_options)

    def run_test(self,test_name):
        try:
            eval(str(ClassGenerator.generate_class(test_name)))(self.driver)
            # if test_name == "test_login":
            #     print("Running test_login...")
            #     test_login.run(self.driver)
            # elif test_name == "test_logout":
            #     print("Running test_logout...")
            #     test_logout.run()
            # else:
            #     print(f"Test {test_name} not found.")
        except Exception as e:
            logging.error(f"Error while running {test_name}: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main = Main()
        main.run_test(sys.argv[1])
    else:
        print("Please specify a test to run. Available tests: test_login, test_logout")