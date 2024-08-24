import os
import sys
import logging
from selenium import webdriver
import tests.test_login as test_login
import tests.test_logout as test_logout

class Main:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def run_test(self,test_name):
        try:
            if test_name == "test_login":
                print("Running test_login...")
                test_login.run(self.driver)
            elif test_name == "test_logout":
                print("Running test_logout...")
                test_logout.run()
            else:
                print(f"Test {test_name} not found.")
        except Exception as e:
            logging.error(f"Error while running {test_name}: {str(e)}")

if __name__ == "__main__":

    if len(sys.argv) > 1:
        main = Main()
        main.run_test(sys.argv[1])
    else:
        print("Please specify a test to run. Available tests: test_login, test_logout")