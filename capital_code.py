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
