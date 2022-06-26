import time
from turtle import delay
from selenium import webdriver
from src.Utils.Methods import Methods
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import json



class BrowserGoogle:
    def __init__(self, dt_start, dt_end):
        print('...Initialize ServerData...')
        self.options = Options()
        self.options.headless = False
        self.driver = webdriver.Chrome(executable_path=r'driver_web_tools\chromedriver.exe', options=self.options)
        self.dt_start = dt_start
        self.dt_end = dt_end
        self.method = Methods()
    
    def getting_value_data(self):
        load = self.method.prepear_data_load_google_json()
        new_dt_start = self.method.convert_data_google_to_request(self.dt_start)
        new_dt_end = self.method.convert_data_google_to_request(self.dt_end)
        self.driver.get(load['site_access'].format(new_dt_start, new_dt_end))
        time.sleep(1)

        all_values_reverer_google_xpath_data_load = self.method.site_xpath_configuration_access()

        ## input origin
        clear_event = self.driver.find_element(By.XPATH, all_values_reverer_google_xpath_data_load[0]).clear()
        time.sleep(1)
        click_event = self.driver.find_element(By.XPATH, all_values_reverer_google_xpath_data_load[0]).click()
        time.sleep(1)

        try:
            locale_into = self.driver.find_element(By.XPATH, all_values_reverer_google_xpath_data_load[0]).send_keys('Fortaleza')
        except:
            pass

        ## input dest
        time.sleep(1)
        destiny_to_fly = self.driver.find_element(By.XPATH, all_values_reverer_google_xpath_data_load[1])
        time.sleep(1)
        destiny_to_fly.click()
        time.sleep(1)
        new_input_text = self.driver.find_element(By.XPATH, all_values_reverer_google_xpath_data_load[2])
        new_input_text.send_keys('Val-de-Cans – Júlio Cezar')
        time.sleep(1)
        new_input_text.send_keys(Keys.ENTER)
        time.sleep(1)

        ## input firstDate
        date_one = self.driver.find_element(By.XPATH, all_values_reverer_google_xpath_data_load[3]).click()
        self.method.Interact_form_flight_google(self.dt_start, self.dt_end)
        self.driver.execute_script(all_values_reverer_google_xpath_data_load[4])
        time.sleep(4)
        scrap_data_load_length = self.driver.execute_script(all_values_reverer_google_xpath_data_load[5])
        value_data_load_length_to_others = scrap_data_load_length / 3
        count = 0
        for i in range(scrap_data_load_length):
                if i < value_data_load_length_to_others:
                    _ = self.driver.execute_script(str(all_values_reverer_google_xpath_data_load[6]).format(i))
                    _ = self.driver.execute_script(str(all_values_reverer_google_xpath_data_load[7]).format(i))
                try:
                    return_price_of_ticket_airline = self.driver.execute_script(str(all_values_reverer_google_xpath_data_load[8]).format(count))
                except:
                    pass
                price_value = str(return_price_of_ticket_airline).replace('\xa0', '')
                price_value = price_value.replace('.', '')
                price_value = price_value.replace('R$', '')
                price_value = int(price_value)
                
                if price_value <= 679:
                    self.method.Sending(self.dt_start, self.dt_end, price_value)
                    break
                count = count + 3
                print(price_value)
        print('...Finish Search in Google...')