import sys, configparser, random

import livestreamer
import cv2

def create_config(Config):
	cfg = open('config', 'w')

	Config.add_section('URLs')
	Config.set('URLs', 'streamList', 'https://www.youtube.com/watch?v=cIL6cKQd1Ls')

	Config.write(cfg)
	cfg.close()

def read_config(Config):
	raw = Config.get('URLs', 'streamList')

	urlList = list(filter(None, (x.strip() for x in raw.splitlines())))

	streamList = []
	for url in urlList:
		try:
			stream = livestreamer.streams(url)['best']
			streamList.append(stream)
		except:
			print("Error: couldn't fetch video stream for url " + url)

	return streamList


# Config setup
Config = configparser.ConfigParser()

if not Config.read('config'):
	 create_config(Config)

streams = read_config(Config)

if streams:
	randSel = random.randint(0, len(streams) - 1)

	stream = streams[randSel]

	cap = cv2.VideoCapture(stream.url)
	isFine, frame = cap.read()
	cap.release()

	if isFine:
		cv2.imwrite('background.png', frame)

else:
	print("No streams available!")
