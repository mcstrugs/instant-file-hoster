#!/bin/sh

if [ -z "$1" ]; then
    echo "[Error]: No path specified"
    echo "Usage: ./build.sh <path/to/file>"
    exit 1
fi

rm -r output
cp -r ./template ./output

python3 setport.py "$1"
