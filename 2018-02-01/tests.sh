#!/bin/sh

DEF_TIME=`stat -c %Z programa.py`

while true
do
	MOD_TIME=`stat -c %Z programa.py`

	if [[ "$MOD_TIME" != "$DEF_TIME" ]] 
	then
	    #echo "programa.py modified"
	    python programa.py
	    
		if [ "$?" = "0" ]
	    then
			#echo "green"
	    	http 192.168.12.38/gpio/green > /dev/null
	    else
			#echo "red"	  	
			http 19.168.12.38/gpio/red > /dev/null
	    fi
	    
	    DEF_TIME=$MOD_TIME
	fi
	sleep 1
done
