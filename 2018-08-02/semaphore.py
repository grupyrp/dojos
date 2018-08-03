#!/usr/bin/env python3
# Script para chamar outro script em caso de modificação

from os import path, system
from time import sleep
import requests

file = './programa.py'
url = 'http://192.168.20.72/set?{}=on'

create_time = path.getctime(file)

while True :
        mod_time = path.getmtime(file)
        if mod_time != create_time:
                exit_status = system(file)
                if exit_status == 0:
                        requests.get(url.format('green'))
                else:
                        requests.get(url.format('red'))
                create_time = mod_time

        sleep(1)
