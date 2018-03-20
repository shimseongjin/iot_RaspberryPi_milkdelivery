
import time
from grovepi import *
import math
import grovepi
from time import sleep
import os

buzzer_pin = 2		#Port for buzzer
button = 5		#Port for Button
dht_sensor_port = 7 	#Port for dht_sensor
dht_sensor_type = 0
ultrasonic_ranger = 4	#Port for Ultrasonic_ranger

distant =0
down_flag=1			#button_flag
temp_flag=1			#temp_flag

pinMode(buzzer_pin,"OUTPUT")	# Assign mode for buzzer as output
pinMode(button,"INPUT")		# Assign mode for Button as input
while True:
	try:
		button_status= digitalRead(button)	#Read the Button status
		distant = ultrasonicRead(ultrasonic_ranger)
		if button_status:	#If the Button is in HIGH position, run the program
			
			if down_flag :
				#button alarm
				print("button push")
				down_flag=0
				str_sample='nodejs fcm-pushserver2.js m_on'
				os.system(str_sample)
				
			[ temp,hum ] = dht(dht_sensor_port,dht_sensor_type)		
			print("temp =", temp, "C\thumidity =",hum,"%", "distance=",distant)
			if (temp>=22)&(temp_flag==1) :
				print("temp= ", temp) 
				#push alarm //expecting
				str_sample='nodejs fcm-pushserver2.js m_on '+str(temp)+' '+str(hum)
				os.system(str_sample)
				temp_flag=0
				sleep(0.5)
				
			if distant>=50 :
				digitalWrite(buzzer_pin,1)
				print("distance= ",distant)
			else :
				digitalWrite(buzzer_pin,0)
			sleep(0.05)

		else:		#If Button is in Off position, print "Off" on the screen
			if down_flag==0 :
				temp_flag=1
				down_flag=1
				print("button pull")
				#pull alarm
				
				str_sample='nodejs fcm-pushserver2.js m_off'
				os.system(str_sample)
			digitalWrite(buzzer_pin,0)		
	except KeyboardInterrupt:	# Stop the buzzer before stopping
		print("key")
		sleep(1)		
		digitalWrite(buzzer_pin,0)
		break
	except (IOError,TypeError) as e:
		print("Error")
