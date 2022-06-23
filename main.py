from selenium.common.exceptions import NoSuchElementException
from time import sleep
from src.decolar.browser import Browser
import sys



if __name__ == '__main__':
    dt_start = sys.argv[1]
    dt_end = sys.argv[2]

    try:
        browser = Browser(dt_start, dt_end)
        browser.getting_value_data()
        sleep(1)
        print('...Finish Search...')

    except Exception as exception:
        print(exception)

    finally:
        pass