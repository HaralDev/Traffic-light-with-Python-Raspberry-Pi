import wiringpi as wp
from time import sleep

# Sequential pin numbering
wp.wiringPiSetupPhys()

wp.pinMode(3,0)
wp.pinMode(11,1) # Red car pin
wp.pinMode(12,1) # Orange car pin
wp.pinMode(13,1) # Green car pin
wp.pinMode(15,1) # Red ped pin
wp.pinMode(16,1) # Green ped pin

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