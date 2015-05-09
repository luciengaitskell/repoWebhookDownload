#!/bin/bash

cd /var/www/Website-SST


#if [ -d "Website-SST-master" ]; then
#  sudo rm -rf Website-SST-master
#fi

#if [ -f "master.zip" ]; then
#  sudo rm master.zip
#fi



wget -N https://github.com/luciengaitskell/Website-SST/archive/master.zip
sudo unzip master.zip
