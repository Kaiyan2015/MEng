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
		operation = input('Input number 0~9 to perform operation, or \'q\' to exit: ')
		if operation == 'q':
			break
		elif operation == '0':
			for i range(8):
				GPIO.OUTPUT(GPIO_OUT[i], 0)
		elif operaion == '1':
			GPIO.OUTPUT(GPIO_OUT[0], 1)
		elif operaion == '2':
			GPIO.OUTPUT(GPIO_OUT[1], 1)
		elif operaion == '3':
			GPIO.OUTPUT(GPIO_OUT[2], 1)
		elif operaion == '4':
			GPIO.OUTPUT(GPIO_OUT[3], 1)
		elif operaion == '5':
			GPIO.OUTPUT(GPIO_OUT[4], 1)
		elif operaion == '6':
			GPIO.OUTPUT(GPIO_OUT[5], 1)
		elif operaion == '7':
			GPIO.OUTPUT(GPIO_OUT[6], 1)
		elif operaion == '8':
			GPIO.OUTPUT(GPIO_OUT[7], 1)
		elif operaion == '9':
			for i in range(8):
				GPIO.OUTPUT(GPIO_OUT[i], 1)
		else:
			pass






		
