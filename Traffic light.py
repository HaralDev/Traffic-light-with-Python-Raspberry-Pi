#==================================
# Traffic light by Haraldeon
#==================================

#=====================
# Importing modules
import wiringpi as wp
from time import sleep
import time as t

#=====================
# Numbering setting, I chose physical ...
# refer to https://github.com/WiringPi/WiringPi-Python
# for more settigns
wp.wiringPiSetupPhys()

#=====================
# Defining the pins

wp.pinMode(3,0)  # Ground pin, warning: keep this as input
wp.pinMode(11,1) # Red car pin
wp.pinMode(12,1) # Orange car pin
wp.pinMode(13,1) # Green car pin
wp.pinMode(15,1) # Red pedestrian pin
wp.pinMode(16,1) # Green pedestrian pin

dt = 0.2         # Determines how fast the lights will blink
def blink(n):
    wp.digitalWrite(11,n) 
    wp.digitalWrite(12,n)
    wp.digitalWrite(13,n)
    wp.digitalWrite(15,n)
    wp.digitalWrite(16,n)
    sleep(dt)

blink(0)         # Resets all the lights to off

t0 = t.time()    # Current time calculation

while  t.time()-t0 <= 10:        # 10 is the amount of seconds you want the sim to run
    wp.digitalWrite(13,1)        # Cars have green  by default
    wp.digitalWrite(15,1)        # Peds have red by default
    if wp.digitalRead(3) == 0:
        #print("Button was clicked, go peds go!") # Remove the '#' if you want to check if your button works
        sleep(1)
        wp.digitalWrite(13,0)    # Button pushed ...
        wp.digitalWrite(12,1)    # Cars get orange
        sleep(3)              
        wp.digitalWrite(12,0)    # From orange 
        wp.digitalWrite(11,1)    # to red for cars
        sleep(1)                 # More buffer for idiots
        wp.digitalWrite(15,0)    # 1 s later ...
        wp.digitalWrite(16,1)    # Peds get green for 3 s
        sleep(3)
        wp.digitalWrite(16,0)    # Peds get ...
        wp.digitalWrite(15,1)    # Red again
        sleep(1)
        wp.digitalWrite(11,0)    # Cars red goes off ...
        wp.digitalWrite(13,1)    # Cars get green again
        sleep(2)
    
    # Loop repeats

print("Program ran for ",t.time()-t0, "seconds")    # Printing how long the program ran

# Blink 3 times when sim ends
blink(0)
blink(1)
blink(0)
blink(1)
blink(0)
blink(1)
blink(0)
