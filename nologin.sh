#!/bin/sh

#
# usage: ./nologin.sh for block anyone login
#        ./nologin.sh <arg> for unlock
#

if [ -z $1 ]; then
    echo "setup nologin"
    sudo touch /etc/nologin
    echo "System down for maintenance, try again later" | sudo tee /etc/nologin
else
    echo "unset nologin"
    sudo rm /etc/nologin
fi
