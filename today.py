#!/usr/bin/python3
import os
import glob
import re
from datetime import datetime
import shutil


print(os.getcwd())
d = {}
for x in glob.glob("*.doc?"):
    y = re.sub("20[2-9][2-9][01][0-9][0-3][0-9]", datetime.now().strftime("%Y%m%d"), x)
    d[x] = y
    print(x, "will be moved to", y)

if input("Proceed? (Y/N)").lower() == 'y':
    for x, y in d.items():
        shutil.move(x, y)

