# liveframe
Grab and save an image from a livestream

## requirements
* opencv (3.2.0 min)

* livestreamer

## installation
Simply run ```setup.py```

check notes below

## usage
```bash
python liveframe.py your_url
```

This ouputs a file to the scripts directory called 'background.png'

Livestreamer automatically pulls the best quality stream available

## notes
* To decode the stream correctly, opencv needs ffmpeg. Sometimes it doesn't link when installing through pip.

	* Livestreamer doesn't gives any heads up and just fails decoding the frame.

	* Best approach I found was installing it through your distros package manager

	* ```sudo pacman -S opencv```
