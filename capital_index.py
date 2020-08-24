import re
import sys
import yaml
import time
from base import Countries

if len(sys.argv) < 2:
    print("Argument (country index) is missing")
    sys.exit(1)
elif not re.match(r"^[0-9]{1,3}$", sys.argv[1]):
    print("Argument (country index) must be a digit 1 - 250")
    sys.exit(1)

index = sys.argv[1]

if int(index) > 250:
    print("Index must be between 1 - 250")
    sys.exit(1)

with open("./config.yml", "r") as config:
    cfg = yaml.safe_load(config)

url = cfg['api'].get('url')

o = Countries(url)
start = time.time()

print("\nCountry Index: \t" + index + " [" + o.get_country_by_index(int(index)) + "]" + "\nCapital: \t" + o.get_capital_by_index(int(index)))

finish = time.time()

print("\n[Response time: ", round(finish - start, 2), " seconds]")
