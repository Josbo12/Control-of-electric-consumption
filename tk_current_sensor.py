#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import random
import time
#import serial


class PowerServer(object):

        def __init__(self):
            super(PowerServer, self).__init__()



        def read_sensor(self):

            #    try:


                               self.a = random.randrange(10)
                               self.b = random.randrange(50)
                               self.c = random.randrange(100)

                               #response = ser.readline()
                               #self.z = response.split(",")
                               #self.z.pop()
                               #self.z = map(float, self.z)

                               #for i in range(len(self.z)):
                                #   self.z[i]=int(self.z[i])

                               #if len(self.z)>=2:
                                #   self.insert_data()




                #except KeyboardInterrupt:
                #    print "Lectura aturada per teclat"



if __name__ == "__main__":

        c = PowerServer()
        c.read_sensor()