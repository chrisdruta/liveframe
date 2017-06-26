# liveframe
Get the lateat frame of a live youtube video

# requirements
opencv (3.2.0 min)

livestreamer
```bash
sudo pip install livestreamer
```

<br />

___note: to decode the stream correctly, opencv needs ffmpeg. Sometimes it doesn't link when installing through pip.
livestreamer doesn't gives any heads up and just fails decoding the frame.___

<br />

Best approach I found was installing it through your distros package manager

```bash
sudo pacman -S opencv
```
