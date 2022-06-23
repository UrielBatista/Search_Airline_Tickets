from selenium import webdriver
from src.Utils.Methods import Methods
from selenium.webdriver.chrome.options import Options

class Browser:
    def __init__(self, dt_start, dt_end):
        print('...Initialize ServerData...')
        self.options = Options()
        self.options.headless = True
        self.driver = webdriver.Chrome(executable_path=r'driver_web_tools\chromedriver.exe', options=self.options)
        self.dt_start = dt_start
        self.dt_end = dt_end
        self.method = Methods()
    
    def getting_value_data(self):
        load = self.method.prepear_data_load_json()
        new_dt_start = self.method.convert_data_to_request(self.dt_start)
        new_dt_end = self.method.convert_data_to_request(self.dt_end)
        self.driver.get(load['site_access'].format(new_dt_start, new_dt_end))
        self.waiting_element_screen(load['script_waiting_page'], load['class_name'])
        lenght = self.executor_script_in_decolar_value('length', 0, load['script_lenth_cards'], load['class_name'])
        for i in range(lenght):
            value_card = self.executor_script_in_decolar_value('value_card', i, load['script_take_value_card'], load['class_name'])
            value_final = self.method.module_data_regex(value_card)
            
            if int(value_final) <= 600:
                print('Valor desejado encontrado: {}'.format(value_final))
                self.method.Sending(self.dt_start, self.dt_end, value_final)
                break

            print("Valores das passagens: R${}".format(value_final))
        
        self.driver.quit()
        # self.driver.close()

    def waiting_element_screen(self, script_waiting_page: str, class_name: str):
        flag = True
        while(flag):
            try:
                result = self.driver.execute_script(script_waiting_page.format(class_name))
                if len(result) > 0:
                    flag = False
            except Exception as e:
                continue

    def executor_script_in_decolar_value(self, case: str, loop: int, script: str, class_name: str):
        if case == 'length':
            result = self.driver.execute_script(script.format(class_name))
        elif case == 'value_card':
            result = self.driver.execute_script(script.format(class_name, loop))
        
        return result