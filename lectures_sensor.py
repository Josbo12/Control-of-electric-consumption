#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import random
import time
import serial
from database import Database

class PowerServer(object):

        def __init__(self):
            super(PowerServer, self).__init__()
            self.database = Database()

        def read_sensor(self):

            while True:
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
                    print self.z
                    #Convertim a int ja que influx només accepta int
                    for i in range(len(self.z)):
                            self.z[i]=int(self.z[i])
                    self.database.insert_data(self.z[0], self.z[1], self.z[2])
                    break

                 except:
                    print "Lectura aturada per teclat"
                    ser.close()


if __name__ == "__main__":

        c = PowerServer()
        c.read_sensor()
