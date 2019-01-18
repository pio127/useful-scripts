#!/bin/bash
if [ $# -eq 3 ]
    then
		find $1 -name "*.$2" -exec grep $3 {} {}>./found_$2_$3.txt \;
	else
    	echo "Three arguments needed: 
			1. Path where to start.
			2. Files extension of text files.
			3. Searched phrase."
fi
