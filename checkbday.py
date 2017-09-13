#!/usr/bin/env python3

# checks if there are any birthdays today and updates the DB accordingly
# to be run once a day
import time
import datetime
from utils import *

data = read_data() # read all data
today = datetime.datetime.now()
today_string = "%02d/%02d"%(today.day, today.month)

for person in data:
    if person.get("birthday") == today_string:
        person["tosend"] = 'True'
update_data(data)



