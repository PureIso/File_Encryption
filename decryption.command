#!/bin/bash
clear
cd "$(dirname "$0")"
python main.py decrypt mytext.txt.encrypted passwordpassword
echo Done