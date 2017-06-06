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

<<<<<<< HEAD
                try:


                                                              
                               ser = serial.Serial('/dev/ttyAMA0', 38400, timeout=1)                               
			       
                               response = ser.readline()
                               self.z = response.split(",")
                               
                               self.z = map(float, self.z)
=======
            #    try:
                               self.a = random.randrange(10)
                               self.b = random.randrange(50)
                               self.c = random.randrange(100)
>>>>>>> bbe3a8fe009b5a0b66f25097e454d6f67cf40997

                               for i in range(len(self.z)):
                                   self.z[i]=int(self.z[i])

                               if len(self.z)>=2:
                                   print "power 1 %s watts" % z[0]
                                   print "power 2 %s watts" % z[1]

                                   print "power 1 %s watts" % z[2][:-2]

<<<<<<< HEAD




=======
                #except KeyboardInterrupt:
                #    print "Lectura aturada per teclat"
>>>>>>> bbe3a8fe009b5a0b66f25097e454d6f67cf40997

                except KeyboardInterrupt:
                    print "Lectura aturada per teclat"

<<<<<<< HEAD
                    ser.close()

=======
>>>>>>> bbe3a8fe009b5a0b66f25097e454d6f67cf40997
if __name__ == "__main__":

        c = PowerServer()
        c.read_sensor()
