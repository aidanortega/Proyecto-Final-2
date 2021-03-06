from urllib import request
import json

class TemperatureManager():
    class Constants:
        base_url = "http://api.openweathermap.org/data/2.5/weather?q=Coyoacan,MX&APPID={}"
        kelvin_temperature = 273.15
        main_key = "main"
        temperature_key = "temp"

    @classmethod
    def get_temperature(cls):
        try:
            with request.urlopen(cls.Constants.base_url) as response:
                data = response.read().decode()
                json_data = json.loads(data)
                variable_aux = json_data[cls.Constants.main_key]
                temperature = float(variable_aux[cls.Constants.temperature_key]) - cls.Constants.kelvin_temperature

                return temperature
        except Exception as error:
            print('Error')