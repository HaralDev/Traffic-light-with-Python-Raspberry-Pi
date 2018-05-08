import wiringpi as wp
from time import sleep
import time as t

# Sequential pin numbering
wp.wiringPiSetupPhys()

wp.pinMode(3,0)
wp.pinMode(11,1) # Red car pin
wp.pinMode(12,1) # Orange car pin
wp.pinMode(13,1) # Green car pin
wp.pinMode(15,1) # Red ped pin
wp.pinMode(16,1) # Green ped pin

print(wp.digitalRead(3))
n = 0
wp.digitalWrite(11,n)
wp.digitalWrite(12,n)
wp.digitalWrite(13,n)
wp.digitalWrite(15,n)
wp.digitalWrite(16,n)

i = 0

t0 = t.time()
while  t.time()-t0 <= 10:
    wp.digitalWrite(13,1) # Cars have green  by default
    wp.digitalWrite(15,1) # Peds have red by default
    if wp.digitalRead(3) == 0:
        print("Button was clicked, go peds go!")
        sleep(1)
        wp.digitalWrite(13,0) # Button pushed ...
        wp.digitalWrite(12,1) # Cars get orange
        sleep(3)              
        wp.digitalWrite(12,0) # From orange 
        wp.digitalWrite(11,1) # to red for cars
        sleep(1)              # More buffer for idiots
        wp.digitalWrite(15,0) # 1 s later ...
        wp.digitalWrite(16,1) # Peds get green for 3 s
        sleep(3)
        wp.digitalWrite(16,0) # Peds get ...
        wp.digitalWrite(15,1) # Red again
        sleep(1)
        wp.digitalWrite(11,0) # Cars red goes off ...
        wp.digitalWrite(13,1) # Cars get green again
        sleep(2)
    # Loop repeats
print("Program run for ",t.time()-t0, "seconds")    

# Blink 3 times when sim ends
dt = .2

def blink(n):
    wp.digitalWrite(11,n)
    wp.digitalWrite(12,n)
    wp.digitalWrite(13,n)
    wp.digitalWrite(15,n)
    wp.digitalWrite(16,n)
    sleep(dt)

blink(0)
blink(1)
blink(0)
blink(1)
blink(0)
blink(1)
blink(0)