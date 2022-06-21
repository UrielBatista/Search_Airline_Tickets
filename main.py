from selenium.common.exceptions import NoSuchElementException
from time import sleep
from src.decolar.browser import Browser

dt_start = '04/07/2022'
dt_end = '08/07/2022'

if __name__ == '__main__':
    try:
        browser = Browser(dt_start, dt_end)
        browser.getting_value_data()
        sleep(1)
        print('...Finish Search...')

    except Exception as exception:
        print(exception)

    finally:
        pass