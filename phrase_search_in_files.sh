#!/bin/bash
if [ $# -eq 3 ]
    then
		find $1 -name "*.$2" -exec grep $3 {} {}>./found_$3_in_$2_files.txt \;
	else
    	echo "Three arguments needed: "
		echo	"	1. Path where to start."
		echo	"	2. Name of file extension of text files."
		echo	"	3. Phrase that needs to be found in text files."
fi
