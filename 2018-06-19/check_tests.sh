#!/bin/sh

DEF_TIME=`stat %Z programa.py`

while true
do
	MOD_TIME=`stat %Z programa.py`

	if [[ "$MOD_TIME" != "$DEF_TIME" ]] 
	then
	    #echo "programa.py modified"
	    python programa.py
	    
		#if [ "$?" = "0" ]
		#then
		##echo "green"
		#http 192.168.25.75/set?green=on > /dev/null
		#else
		##echo "red"
		#http 192.168.25.75/set?red=on > /dev/null
		#fi
	    
	    DEF_TIME=$MOD_TIME
	fi
	sleep 1
	echo -n "."
done
