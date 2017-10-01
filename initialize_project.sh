#!/bin/bash
if ! [ "$1" = "--no-install" ]; then
    sudo apt-get install virtualenv
    sudo apt-get install python3
fi
