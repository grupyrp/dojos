#!/bin/sh

while true
do
    sleep 1
    clear
    python programa.py
    if [ "$?" = "0" ]; then
        http 192.168.12.38/gpio/green > /dev/null
    else
        http 192.168.12.38/gpio/red > /dev/null
    fi
done
