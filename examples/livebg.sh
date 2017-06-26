#!/bin/bash
default="http://www.youtube.com/watch?v=ZMgzWbBzbQE"

if [$2 == ""]; then
	url=$default
else
	url=$2

fi

while true
do
    python liveframe.py $url
    feh --bg-scale background.png
		sleep $1
done
