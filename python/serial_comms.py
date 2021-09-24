import serial
import time
arduino = serial.Serial(port='/dev/ttyACM1', baudrate=115200, timeout=.1)

def write_to_servo_both(x,y):
    
    arduino.write(bytes('m,', 'utf-8'))
    arduino.write(bytes(x, 'utf-8'))
    arduino.write(bytes(',', 'utf-8'))
    arduino.write(bytes(y, 'utf-8'))
    arduino.write(bytes('eom', 'utf-8'))
    time.sleep(.05)
    data = arduino.readline()
    return data

def write_to_servo1(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(.05)
    data = arduino.readline()
    return data

while True:
    num1 = input("what position x?: ") # Taking input from user
    num2 = input("what position y?: ")
    if num1 == "q":
        break
    #if num2 == "q":
    #    break
    value = write_to_servo_both(num1, num2)
    print(value) # printing the value

