import requests
import json


class Countries:

    def __init__(self, url):
        self.url = url

    def get_all(self):
        r = requests.get(self.url + '/rest/v2/all?fields=name;capital;alpha3Code')
        value = json.loads(r.text)
        if r.status_code == 200:
            for i in range(len(value)):
                print(str(i + 1) + '. Country: ' + value[i].get("name") + '[' + value[i].get(
                    "alpha3Code") + ']' + '; Capital: ', value[i].get("capital"))
        else:
            print('API Returns an error')

    def get_capital_by_index(self, index):
        r = requests.get(self.url + '/rest/v2/all?fields=name;capital;alpha3Code')
        value = json.loads(r.text)
        if r.status_code == 200:
            return value[index - 1].get("capital")
        else:
            return 'API Returns an error: Index must be between 1 and 250'

    def get_country_by_index(self, index):
        r = requests.get(self.url + '/rest/v2/all?fields=name;alpha3Code')
        value = json.loads(r.text)
        if r.status_code == 200:
            return value[index - 1].get("name")
        else:
            return 'API Returns an error: Index must be between 1 and 250'

    def get_capital_by_code(self, code):
        r = requests.get(self.url + '/rest/v2/alpha/' + code + '?fields=capital')
        value = json.loads(r.text)
        if r.status_code == 200:
            return value.get("capital")
        else:
            return 'API Returns an error: Country Code does not exist'


    def get_capital_by_country_name(self, name):
        r = requests.get(self.url + '/rest/v2/name/' + name + '?fields=capital')
        value = json.loads(r.text)
        if r.status_code == 200:
            return value[0].get("capital")
        else:
            return 'API Returns an error: Country Name does not exist'

