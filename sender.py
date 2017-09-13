#!/usr/bin/env python3

# extra module to be run on an hourly basis in order to be able to send email
# as and when internet connection is available
import os
from utils import *

data = read_data()

for person in data:
    if person.get("tosend") == 'True':
        notif_command = 'notify-send "Birthday mail" "Sending mail to {name}" -t 3000'.format(name=person.get('name'))
        os.system(notif_command)
        if(make_send_message(person)):
            notif_command = 'notify-send "Birthday mail" "Mail successfully sent to {name}" -t 3000'.format(name=person.get('name'))
            os.system(notif_command)
            person["tosend"] = 'False'
update_data(data)

