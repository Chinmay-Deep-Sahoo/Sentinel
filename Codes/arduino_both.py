from pyfirmata import Arduino, SERVO, util
from time import sleep

port = 'COM6'
pin1 = 10
pin2 = 9

board = Arduino(port)

board.digital[pin1].mode = SERVO
board.digital[pin2].mode = SERVO

def rotateservo(pin, angle):
    board.digital[pin].write(angle)
    sleep(0.015)

while True:
    x = input("input (PIN 1) (PIN 2): ").split(" ")
    x = [int(i) for i in x]
    x,y = x
    
    # if x == "1":
    #     for i in range(50,120):
    #         rotateservo(pin, i)
    # elif x == "2":
    #     for i in range(0,90):
    #         rotateservo(pin, i)
    # elif x == "3":
    #     for i in range(0, 270):
    #         rotateservo(pin, i)
    rotateservo(pin1, x)
    rotateservo(pin2, y)