#!/bin/bash
clear
cd "$(dirname "$0")"
python main.py encrypt mytext.txt passwordpassword
echo Done