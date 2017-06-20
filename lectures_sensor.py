#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import random
import time
import serial

class PowerServer(object):

        def __init__(self):
            super(PowerServer, self).__init__()



        def read_sensor(self):


                 try:
                     
                    ser = serial.Serial('/dev/ttyAMA0', 38400, timeout=1)
                    #Obtenim resposta del port serial
                    response = ser.readline()
                    #separem resposta en comes
                    self.z = response.split(",")
                    #eliminem els salts de linia que puguin apareixer
                    self.z = [x.replace("\r\n","") for x in self.z]
                    #convertim els valors string en float
                    self.z = map(float, self.z)

                    #Convertim a int ja que influx només accepta int
                    for i in range(len(self.z)):
                            self.z[i]=int(self.z[i])

                 except KeyboardInterrupt:
                    print "Lectura aturada per teclat"
                    ser.close()


if __name__ == "__main__":

        c = PowerServer()
        c.read_sensor()
