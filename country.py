import re
import sys
import yaml
import time
from base import Countries

if len(sys.argv) < 2:
    print("Argument (country name file) is missing")
    sys.exit(1)
elif not re.match("[A-Za-z]{3}", sys.argv[1]):
    print("Argument (country name file) must be: 'csv' file")
    sys.exit(1)

input_file = sys.argv[1]

with open("./config.yml", "r") as config:
    cfg = yaml.safe_load(config)

url = cfg['api'].get('url')

o = Countries(url)
start = time.time()

with open(input_file, "r") as names:
    for name in names:
        print("--------------------------------")
        print("Country Name: \t" + name + "Capital: \t" + o.get_capital_by_country_name(name.strip()))

finish = time.time()
print("--------------------------------")
print("[Response time: ", round(finish - start, 2), " seconds]")

# o.get_capital_by_code('lva')
# o.get_capital_by_country_name('Latvia')
# o.get_by_index(124)
# o.get_all()
