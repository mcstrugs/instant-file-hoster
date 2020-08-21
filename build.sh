#!/bin/bash

if [ "$1" == "" ]; then
    echo "[Error]: No path specified"
    echo "Usage: ./build.sh <path/to/file>"
    exit 1
fi

rm -r output
cp -r ./template ./output
cp -r $1 ./output/files/.

python3 setport.py
