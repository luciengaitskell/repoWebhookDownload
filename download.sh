#!/bin/bash

cd $1


if [ -d "$2-$3" ]; then
  sudo rm -rf $2-$3
fi

if [ -f "$3.zip" ]; then
  sudo rm $3.zip
fi



wget -N https://github.com/luciengaitskell/$2/archive/$3.zip
sudo unzip $3.zip
