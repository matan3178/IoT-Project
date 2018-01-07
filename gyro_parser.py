from functools import reduce

class Gyro:
	def __init__(self, pitch, roll, yaw):
		self.roll = roll
		self.pitch = pitch
		self.yaw = yaw

	def __str__(self):
		return ("pitch: "+str(self.pitch)+", roll: "+str(self.roll)+", yaw: "+str(self.yaw))

class Parser:
# def parse(path):
# 	gyros = read_lines(path)
# 	for gyro in gyros:
# 		print(gyro)

	

	def getDerivates(self):
		derivates_pitch = list()
		derivates_roll = list()
		derivates_yaw = list()
		last_pitch = 0;
		last_roll = 0;
		last_yaw = 0;
		for gyro in self.gyros:			
			derivates_pitch.append(gyro.pitch - last_pitch)
			derivates_roll.append(gyro.roll - last_roll)
			derivates_yaw.append(gyro.yaw - last_yaw)
			last_pitch = gyro.pitch
			last_roll = gyro.roll
			last_yaw = gyro.yaw
		return derivates_pitch,derivates_roll,derivates_yaw

	def printDerivates(self):
		pitch,roll,yaw = self.getDerivates()
		print(pitch)
		print(roll)
		print(yaw)
		
	def printStatistics(self):
		pitch,roll,yaw = self.getDerivates()
		print ("pitch avg: "+ str(self.getAVG(pitch)))
		print ("roll avg: "+ str(self.getAVG(roll)))
		print ("yaw avg: "+ str(self.getAVG(yaw)))
		print ("pitch max: "+ str(max(pitch)))
		print ("roll max: "+ str(max(roll)))
		print ("yaw max: "+ str(max(yaw)))
		print ("pitch min: "+ str(min(pitch)))
		print ("roll min: "+ str(min(roll)))
		print ("yaw min: "+ str(min(yaw)))

	def getAVG(self, lst):
		return float(sum(lst)) / max(len(lst), 1)

	def __init__(self, path):
		with open(path) as f:
		    content = f.readlines()
		# print(content)
		content = [strip(x) for x in content] 
		# print(content)
		gyro_list = list()
		for c in content:
			arr = c.split(', ')
			gyro_list.append(Gyro(float(arr[0]),float(arr[1]),float(arr[2])))
		self.gyros = gyro_list

	def strip(self, line):
		pass
		line = line.replace('p: ','')
		line = line.replace('r: ','')
		line = line.replace('y: ','')
		line = line.strip()
		return line

def sense():
	from sense_hat import SenseHat
	sense = SenseHat()
	while(1):
		gyro_only = sense.get_gyroscope()
		print("p: {pitch}, r: {roll}, y: {yaw}".format(**gyro_only))