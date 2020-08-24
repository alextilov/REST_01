import re
import sys
import yaml
import time
from base import Countries

if len(sys.argv) < 2:
    print("Argument (country name) is missing")
    sys.exit(1)
elif not re.match(r"[A-Za-z]{4,52}", sys.argv[1]):
    print("Argument (country name) must be an alphabetic 4 - 52 chars long")
    sys.exit(1)

name = sys.argv[1]

with open("./config.yml", "r") as config:
    cfg = yaml.safe_load(config)

url = cfg['api'].get('url')

o = Countries(url)
start = time.time()

print("\nCountry Name: \t" + name + ";\nCapital: \t" + o.get_capital_by_country_name(name))

finish = time.time()

print("\n[Response time: ", round(finish - start, 2), " seconds]")

