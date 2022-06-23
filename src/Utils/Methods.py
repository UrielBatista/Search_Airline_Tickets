import re
import json
import sys
import email
import smtplib

class Methods:

    def __init__(self) -> None:
        self.data_access = open(r'appsetings\settings.json')

    def convert_data_to_request(self, dt_format_old: str):
        value = dt_format_old.split("/")
        day = value[0]
        month = value[1]
        year = value[2]
        new_dt_return = "{}-{}-{}".format(year, month, day)

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
        data = json.load(self.data_access)
        data_load = {}
        data_load["site_access"] = data['data']['browser_config']['site']
        data_load["script_waiting_page"] = data['data']['browser_config']['script_waiting_page']
        data_load["script_lenth_cards"] = data['data']['browser_config']['script_lenth_cards']
        data_load["script_take_value_card"] = data['data']['browser_config']['script_take_value_card']
        data_load["class_name"] = data['data']['browser_config']['class_name']

        return data_load

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