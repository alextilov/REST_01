# REST_01
Capital city based on Country name.

[Standardized QA SDET Code examination]

## Description
A)	Using the provide REST service, create a program that returns, at minimum, capital city based on user input for name or code.

B)	Write several tests that validate positive and negative scenario’s

## Requirements

Python 3.8+

### Packages:
  pyyaml 5.3.1
  
  requests 2.24.0

## Installation

```console
  pip install pyyaml
  pip install requests
  pip install html-testRunner
```
## Project structure

#### config.yml
```python
api:
    url: https://restcountries.eu
```

#### codes.csv
```python
USA
ITA
LVA
CAN
GBR
```

#### all_codes.csv
```python
ABW
--- 250
ZWE
```

#### all_codes.csv
```python
ABW
--- 250
ZWE
```

#### countries.csv
```python
United States of America
Italy
Latvia
Canada
United Kingdom of Great Britain and Northern Ireland
```
#### all_countries.csv
```python
Afghanistan
--- 250
Åland Islands
```

#### base.py
```python
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

```

#### capital_code.py
```python
import re
import sys
import yaml
import time
from base import Countries

if len(sys.argv) < 2:
    print("Argument (country code) is missing")
    sys.exit(1)
elif not re.match(r'[A-Za-z]{3}', sys.argv[1]):
    print("Argument (country code) must be an alphabetic 3 chars long")
    sys.exit(1)

code = sys.argv[1]

with open("./config.yml", "r") as config:
    cfg = yaml.safe_load(config)

url = cfg['api'].get('url')

o = Countries(url)
start = time.time()

print("\nCountry Code: \t" + code + ";\nCapital: \t" + o.get_capital_by_code(code))

finish = time.time()

print("\n[Response time: ", round(finish - start, 2), " seconds]")

```

## Usage

### Error Handling

```console
$ python capital_code.py
Argument (country code) is missing
```

```console
$ python capital_code.py ABC
Country Code:   ABC;
Capital:        API Returns an error: Country Code does not exist
[Response time:  0.28  seconds]
```

```console
$ python capital_name.py
Argument (country name) is missing
```

```console
$ python capital_name.py "Blah Blah"
Country Name:   Blah Blah;
Capital:        API Returns an error: Country Name does not exist
[Response time:  0.22  seconds]
```

```console
$ python capital_index.py
Argument (country index) is missing
```

```console
$ python capital_index.py 300
Index must be between 1 - 250
```

### Return Capital by Country Code

```console
$ python capital_code.py USA

Country Code:   USA;
Capital:        Washington, D.C.
[Response time:  0.25  seconds]
```
### Return Capital by Country Name

```console
$ python capital_name.py "Republic of India"

Country Name:   Republic of India;
Capital:        New Delhi
[Response time:  0.22  seconds]
```

### Return Capital by Country Index

```console
$ python capital_index.py 124

Country Index:  124 [Latvia]
Capital:        Riga
[Response time:  1.48  seconds]
```

### Return Capital by Country Code from File

```console
$ python codes.py codes.csv

--------------------------------
Country Code:   USA
Capital:        Washington, D.C.
--------------------------------
Country Code:   ITA
Capital:        Rome
--------------------------------
Country Code:   LVA
Capital:        Riga
--------------------------------
Country Code:   CAN
Capital:        Ottawa
--------------------------------
Country Code:   GBR
Capital:        London
--------------------------------
[Response time:  2.13  seconds]
```

```console
$ python codes.py all_codes.csv

--------------------------------
Country Code:   ABW
Capital:        Oranjestad
--------------------------------

------------- 250 --------------

--------------------------------
Country Code:   ZWE
Capital:        Harare
--------------------------------
[Response time:  48.71  seconds]
```

### Return Capital by Country Name from File

```console
$ python country.py countries.csv

--------------------------------
Country Name:   United States of America
Capital:        Washington, D.C.
--------------------------------
Country Name:   Italy
Capital:        Rome
--------------------------------
Country Name:   Latvia
Capital:        Riga
--------------------------------
Country Name:   Canada
Capital:        Ottawa
--------------------------------
Country Name:   United Kingdom of Great Britain and Northern Ireland
Capital:        London
--------------------------------
[Response time:  3.18  seconds]
```

```console
$ python country.py all_countries.csv

--------------------------------
Country Code:   ABW
Capital:        Oranjestad
-------------------------------- 

------------- 250 --------------

--------------------------------
Country Name:   Åland Islands
Capital:   Mariehamn
--------------------------------
[Response time:  58.27  seconds]
```
### UnitTest
```console
$ python -m unittest test.py
...
----------------------------------------------------------------------
Ran 3 tests in 0.736s

OK
```
```console
$ python test.py

Running tests...
----------------------------------------------------------------------
 test_country_code (__main__.Test) ... OK (0.000066)s
 test_country_index (__main__.Test) ... OK (0.000034)s
 test_country_name (__main__.Test) ... OK (0.000029)s

----------------------------------------------------------------------
Ran 3 tests in 0:00:00

OK

Generating HTML reports...
test-reports/TestResults_Test_2020-08-24_00-37-36.html
```
--------------------------------

#### test.py
```python
from base import Countries
import yaml
import unittest
import HtmlTestRunner

class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        with open("./config.yml", "r") as config:
            cfg = yaml.safe_load(config)

        url = cfg['api'].get('url')
        o = Countries(url)
        cls.capital_by_code = o.get_capital_by_code("LVA")
        cls.capital_by_name = o.get_capital_by_country_name("Latvia")
        cls.capital_by_index = o.get_capital_by_index(124)

    def test_country_code(self):
        self.assertTrue(self.capital_by_code == "Riga", "Test failed: capital by code")

    def test_country_name(self):
        self.assertTrue(self.capital_by_name == "Riga", "Test failed: capital by name")

    def test_country_index(self):
        self.assertTrue(self.capital_by_index == "Riga", "Test failed: capital by index")

if __name__ == '__main__':
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output='test-reports',
            open_in_browser=True,
            combine_reports=True
            )
        )
```

### Test Result:

![Test Results](http://alex.academy/result.png)

This is a sample of the results.

