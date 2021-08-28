import serial
import sys
import time
import os
print(os.path.dirname(__file__))
#for DUT 
# url = '/dev/cu.usbserial-DUT2'
# command = '[HV]\n'
baudrate = '921600'
#reciveAgs = sys.argv[0]
url = '/dev/tty.kis-14631000-ch-1'
url = sys.argv[1]
#baudrate = '230400'
timeout = 5
command = sys.argv[2]
ser = serial.Serial(url,baudrate,timeout=timeout)
# print(ser.port)
# print("the port status is :",ser.isOpen())
ser.write( bytes(command, encoding="utf8"))
#ser.write( bytes('\n', encoding="utf8"))
time.sleep(0.2)
dataFromSer = ser.readline()
print('dataFromSer is',str(dataFromSer, encoding = "utf8"))
ser.close()
print('test branch')