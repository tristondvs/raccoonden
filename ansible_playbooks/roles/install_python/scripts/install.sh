#!/bin/bash
cd Python-3.7.2/
./configure --enable-optimizations
make altinstall
pip3.7 install --upgrade pip
touch /etc/python_installed
