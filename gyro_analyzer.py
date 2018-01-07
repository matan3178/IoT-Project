import collections
import logger

MAX_LEN = 5
def sense():
	from sense_hat import SenseHat
	import time
	sense = SenseHat()
	last_pitch = 0
	last_roll = 0
	last_yaw = 0
	pitch_queue = collections.deque(maxlen = MAX_LEN)
	roll_queue = collections.deque(maxlen = MAX_LEN)
	yaw_queue = collections.deque(maxlen = MAX_LEN)
	count = 0
	canStart = False
	time_drives = 0
	count_drives = 0
	while 1:
		gyro = sense.get_gyroscope()
		logger.log("p: {pitch}, r: {roll}, y: {yaw}".format(**gyro))
		pitch_queue.append(gyro['pitch'] - last_pitch)
		roll_queue.append(gyro['roll'] - last_roll)
		yaw_queue.append(gyro['yaw'] - last_yaw)
		last_pitch = gyro['pitch']
		last_roll = gyro['roll']
		last_yaw = gyro['yaw']


		if count > MAX_LEN * 2:
			canStart = True
		count += 1

		if canStart:
			pitch_mean = get_mean(pitch_queue)
			roll_mean = get_mean(roll_queue)
			yaw_mean = get_mean(yaw_queue)
			if pitch_mean > 0.7 or roll_mean > 0.5 or yaw_mean > 0.5:
				print('driving')
				time_drives = time.time()
				count_drives += 1
			else:
				if count_drives > 10 and (time.time() - time_drives) > 15:
					count_drives = 0
					logger.log("not driving for a while")
					return True
				else:
					print("not driving...")

		time.sleep(0.4)

def get_mean(lst):
	return float(sum(lst)) / max(len(lst), 1)