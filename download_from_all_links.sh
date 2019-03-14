#!/bin/bash

#  aria2c program must be built or downloaded
#  for Debian: apt-get install
#  for Arch: pacman -S 
if ! [ -x "$(command -v aria2c)" ]; then
	echo "Error: no aria2c found" >&2
	exit 1
fi

if [ $# -eq 1 ]; then
	mkdir "$1"
	cd "$1"
	touch links_to_download.txt
	vim links_to_download.txt
	aria2c --input-file=links_to_download.txt
	rm links_to_download.txt
else
	echo "Folder name must be provided"
	exit 1
fi
