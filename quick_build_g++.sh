#!/bin/bash

vim temp.cpp
g++ temp.cpp -o temp -std=c++17
./temp
echo
rm temp.cpp temp