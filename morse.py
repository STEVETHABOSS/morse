'''
Morse Code Interpreter
By Cyrus Boushehri
30/10/2016
'''

#import RPi.GPIO as GPIO
import time
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(18, GPIO.OUT)

def main():    
    tex = []
    pos = 0
    l = "t"

    while(l == "t"):
        inp = input(">")
        
        if(inp == "q"):
            l = "f"

        elif(inp == "l"):
            tex.append("l")
            l = "f"
            
        elif(inp == "w"):
            tex.append(inp)
        

        elif(inp == "0" or "1"):
            tex.append(int(inp))
	            
        print(tex)
        
    ln = len(tex)
    while (ln > 0):
        
        if(tex[pos] == "l"):
            ln = len(tex)
            pos = 0
            
        elif(tex[pos] == 0):
            dot()
            
        elif(tex[pos] == 1):
            dash()
            
        elif(tex[pos] == 'w'):
            wait()

        pos = pos + 1
        ln = ln - 1


def dot():
    print("dot")
#    GPIO.output(18,GPIO.HIGH)
    time.sleep(.3)
#    GPIO.output(18,GPIO.LOW)
    time.sleep(.1)


def dash():
    print("dash")
#    GPIO.output(18,GPIO.HIGH)
    time.sleep(.5)
#    GPIO.output(18,GPIO.LOW)
    time.sleep(.1)


def wait():
    print("wait")
#    GPIO.output(18,GPIO.LOW)
    time.sleep(.5)
    time.sleep(.1)


main()
