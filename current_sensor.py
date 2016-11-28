#!/usr/bin/python
from influxdb import InfluxDBClient
from influxdb.client import InfluxDBClientError
import datetime
import random
import time
import serial



USER = 'root'
PASSWORD = 'root'
DBNAME = 'powerdb'




ser = serial.Serial('/dev/ttyAMA0', 38400, timeout=1)
host ='localhost'
port = 8086
metric = "powerdata"


class PowerServer(object):

        def __init__(self):
            super(PowerServer, self).__init__()

            self.series = []
            self.z = []

        def read_sensor(self):

                try:
                       while len(self.z)<2 :
                              
                               response = ser.readline()
                               self.z = response.split(",")
                               self.z.pop()
                               self.z = map(float, self.z)
                               print response
                               if len(self.z)==2:
                                  self.z[0]=int(self.z[0])
                                  self.z[1]=int(self.z[1])
                                  print "Power 1: %s  Watts" % self.z[0]
                                  print "Power 2: %s  Watts" % self.z[1]
                                  self.insert_data()
                                  self.z=[]
                               time.sleep(5)   
                except KeyboardInterrupt:
                    print "Lectura aturada per teclat"
                       #ser.close()

        def insert_data(self):

           # try:
               now = datetime.datetime.today()
               hostName = "server-%d" % random.randint(1, 5)
               pointValues = {
                       "time": now.strftime ("%Y-%m-%d %H:%M:%S"),
                       "measurement": metric,
                       "fields":{
                             "Power1": self.z[0],
                             "Power2": self.z[1],
                            # "Power3": z[2][:-2],
                         },
                       "tags": {
                           "hostName": hostName,
                       },
                   }
               self.series.append(pointValues)

               client = InfluxDBClient(host, port, USER, PASSWORD, DBNAME)
               retention_policy = 'awesome_policy'
               client.create_retention_policy(retention_policy, '3d', 3, default=True)
               client.write_points(self.series, retention_policy=retention_policy)
                  
           # except:
            #      print "Error al introduir les dades"
                  
if __name__ == "__main__":
        c = PowerServer()
        c.read_sensor()
