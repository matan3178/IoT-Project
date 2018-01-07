import cameraAnalyzer as camera
import gyro_analyzer as gyro
import time
import os
import logger
def main():
	time.sleep(1)
	threshold = camera.getThreshold()
	if gyro.sense():
		if camera.isThereBaby(threshold):
			alarm()

def alarm():
	logger.log("Baby Needs help")
	os.system('omxplayer -o local alert.mp3')

