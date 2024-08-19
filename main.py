import sys
import logging
import tests.test_login as test_login
import tests.test_logout as test_logout


# ログの設定
logging.basicConfig(filename='test_log.log', level=logging.ERROR,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def run_test(test_name):
    try:
        if test_name == "test_login":
            print("Running test_login...")
            test_login.run()
        elif test_name == "test_logout":
            print("Running test_logout...")
            test_logout.run()
        else:
            print(f"Test {test_name} not found.")
    except Exception as e:
        logging.error(f"Error while running {test_name}: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        test_name = sys.argv[1]
        run_test(test_name)
    else:
        print("Please specify a test to run. Available tests: test_login, test_logout")