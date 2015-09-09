#!/bin/sh

# Install all the python libraries via pip

rm -rf lib/!(README.md)
sudo pip install -r requirements.txt -t lib/