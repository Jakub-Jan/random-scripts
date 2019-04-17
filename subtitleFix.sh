#!/bin/bash
cd $1
find . -name \*.srt -exec file -i {} \; | grep "unknown" | sed 's/: text\/plain\; charset\=unknown\-8bit//' | while read line
do
        cp "$line" "$line".bak
        iconv -f WINDOWS-1250 -t UTF-8 "$line".bak > "$line"
        echo "$line" "OK"
done
