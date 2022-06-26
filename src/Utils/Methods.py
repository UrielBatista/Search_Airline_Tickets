import re
import json
import sys
import email
import smtplib
import time
import keyboard

class Methods:

    def __init__(self) -> None:
        self.data_access = open(r'appsetings\settings.json')
        self.data = json.load(self.data_access)

    def convert_data_to_request(self, dt_format_old: str):
        value = dt_format_old.split("/")
        day = value[0]
        month = value[1]
        year = value[2]
        new_dt_return = "{}-{}-{}".format(year, month, day)

        return new_dt_return

    def convert_data_google_to_request(self, dt_format_old: str):
        value = dt_format_old.split("/")
        day = value[0]
        month = value[1]
        year = value[2]
        new_dt_return = "{}-{}-{}".format(day, month, year)

        return new_dt_return

    def module_data_regex(self, value_card):
        value_price_final = re.findall(r"Preço final R\$+[0-9]{,4}[.]?[0-9]{,10}", value_card)
        value_final = re.sub(r"Preço final R\$+", "", str(value_price_final))
        value_final = value_final.replace('[', '')
        value_final = value_final.replace(']', '')
        value_final = value_final.replace("'", '')
        try:
            value_final = value_final.replace('.', '')
        except:
            pass

        return value_final

    def prepear_data_load_json(self):
        data_load = {}
        data_load["site_access"] = self.data['data']['browser_config']['site']
        data_load["script_waiting_page"] = self.data['data']['browser_config']['script_waiting_page']
        data_load["script_lenth_cards"] = self.data['data']['browser_config']['script_lenth_cards']
        data_load["script_take_value_card"] = self.data['data']['browser_config']['script_take_value_card']
        data_load["class_name"] = self.data['data']['browser_config']['class_name']

        return data_load

    def prepear_data_load_google_json(self):
        data_load = {}
        data_load["site_access"] = self.data['data']['browser_google']['site']

        return data_load

    def site_xpath_configuration_access(self):
        
        origin_to_flight = self.data['data']['browser_google']['origin_to_flight']
        origin_dest_flight = self.data['data']['browser_google']['origin_dest_flight']
        input_text_dest_to_flight = self.data['data']['browser_google']['input_text_dest_to_flight']
        click_date_start = self.data['data']['browser_google']['click_date_start']
        load_all_data_page = self.data['data']['browser_google']['load_all_data_page']
        return_number_of_tickets_airline = self.data['data']['browser_google']['return_number_of_tickets_airline']
        return_interprise_of_flight = self.data['data']['browser_google']['return_interprise_of_flight']
        return_quantity_stoped_of_flight = self.data['data']['browser_google']['return_quantity_stoped_of_flight']
        return_price_of_ticket_airline = self.data['data']['browser_google']['return_price_of_ticket_airline']

        return (origin_to_flight, origin_dest_flight, input_text_dest_to_flight, click_date_start, load_all_data_page, 
            return_number_of_tickets_airline, return_interprise_of_flight, return_quantity_stoped_of_flight, 
            return_price_of_ticket_airline)


    def Sending(self, dt_start, dt_end, value_final):
        recipients = ["ur.sabatista@gmail.com", "tassiasilvatavares@gmail.com"]
        msg = email.message_from_string("Passagem de R${} de acordo com as datas {} - {}".format(value_final, dt_start, dt_end))
        msg['From'] = "uri_airline_tickets@outlook.com"
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = "PASSAGEM ENCONTRADA!!"

        s = smtplib.SMTP("smtp.office365.com",587)
        s.ehlo()
        s.starttls() 
        s.ehlo()
        s.login("uri_airline_tickets@outlook.com", 'airlines@2022')
        s.sendmail("uri_airline_tickets@outlook.com", recipients, msg.as_string())
        print("...Email Sender...")

    def Interact_form_flight_google(self, dt_start, dt_end):
        time.sleep(1)
        keyboard.write('{}'.format(dt_start))
        time.sleep(1)
        keyboard.press('ENTER')
        time.sleep(1)
        keyboard.press('TAB')
        time.sleep(1)
        keyboard.write('{}'.format(dt_end))
        time.sleep(1)
        keyboard.press('ENTER')
        time.sleep(1)
        keyboard.press('ENTER')
        time.sleep(4)