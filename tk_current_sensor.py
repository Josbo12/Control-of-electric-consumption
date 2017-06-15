#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import random
import time

import serial

#ser = serial.Serial('/dev/ttyAMA0', 38400, timeout=1)


class PowerServer(object):

        def __init__(self):
            super(PowerServer, self).__init__()


        def read_sensor(self):


                try:


                               ser = serial.Serial('/dev/ttyAMA0', 38400, timeout=1)

                               self.z = response.split(",")
                               self.z = [x.replace("\r\n","") for x in self.z]
                               #self.z.pop()
                               self.z = map(float, self.z)

                               for i in range(len(self.z)):
                                    self.z[i]=int(self.z[i])

                               if len(self.z)>=2:
                                   print "power 1 %s watts" % z[0]
                                   print "power 2 %s watts" % z[1]

                                   print "power 1 %s watts" % z[2]
                               time.sleep(5)


                


                except KeyboardInterrupt:
                    print "Lectura aturada per teclat"

                    ser.close()


if __name__ == "__main__":

        c = PowerServer()
        c.read_sensor()
