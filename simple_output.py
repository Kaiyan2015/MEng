import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)

GPIO_OUT = [5, 6, 13, 19, 26, 12, 16, 20]

if __name__ == "__main__":
	while 1:
		operation = input('Input number 0~9 to perform operation, or -1 to exit: ')
		if operation == -1:
			break
		elif operation == 0:
			for i in range(8):
				GPIO.output(GPIO_OUT[i], 0)
		elif operation == 1:
			for i in range(8):
				if i == 1:
					GPIO.output(GPIO_OUT[i-1], 1)
				else:
					GPIO.output(GPIO_OUT[i], 0)
			
		elif operation == 2:
			for i in range(8):
				if i == 2:
					GPIO.output(GPIO_OUT[i-1], 1)
				else:
					GPIO.output(GPIO_OUT[i], 0)
		elif operation == 3:
			for i in range(8):
				if i == 3:
					GPIO.output(GPIO_OUT[i-1], 1)
				else:
					GPIO.output(GPIO_OUT[i], 0)
		elif operation == 4:
			for i in range(8):
				if i == 4:
					GPIO.output(GPIO_OUT[i-1], 1)
				else:
					GPIO.output(GPIO_OUT[i], 0)
		elif operation == 5:
			for i in range(8):
				if i == 5:
					GPIO.output(GPIO_OUT[i-1], 1)
				else:
					GPIO.output(GPIO_OUT[i], 0)
		elif operation == 6:
			for i in range(8):
				if i == 6:
					GPIO.output(GPIO_OUT[i-1], 1)
				else:
					GPIO.output(GPIO_OUT[i], 0)
		elif operation == 7:
			for i in range(8):
				if i == 7:
					GPIO.output(GPIO_OUT[i-1], 1)
				else:
					GPIO.output(GPIO_OUT[i], 0)
		elif operation == 8:
			for i in range(8):
				GPIO.output(GPIO_OUT[i], 0)
			GPIO.output(20, 1)
		elif operation == 9:
			for i in range(8):
				GPIO.output(GPIO_OUT[i], 1)
		else:
			pass

	GPIO.cleanup()




		
