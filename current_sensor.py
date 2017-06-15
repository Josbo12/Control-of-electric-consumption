#!/usr/bin/python
from influxdb import InfluxDBClient
from influxdb.client import InfluxDBClientError
import datetime
import random
import time
import serial



USER = 'root'
PASSWORD = 'root'
DBNAME = 'diferencial_db'

ser = serial.Serial('/dev/ttyAMA0', 38400, timeout=1)
host ='localhost'
port = 8086

#metric = "llum_force"
#metric = "trast1_trast2"
#metric = "encim_aire"
#metric = "rent_term2"
metric = "dif1_dif2"

class PowerServer(object):

        def __init__(self):
            super(PowerServer, self).__init__()



        def read_sensor(self):

                try:
                       while True:

                          #  self.a = random.randrange(10)
                         #   self.b = random.randrange(50)
                        #    self.c = random.randrange(100)
                              response = ser.readline()                          
                                                          
                              self.z = response.split(",")
                              self.z = [x.replace("\r\n","") for x in self.z]                   
                              print "eii" 
                              print self.z 
                              #self.z.pop()
                              self.z = map(float, self.z)
                              print "self.z"
                              print self.z
                              for i in range(len(self.z)):
                                   self.z[i]=int(self.z[i])
                                   print self.z[i]
                              time.sleep(5)
                             # if len(self.z)>=2:
                                



                except KeyboardInterrupt:
                    print "Lectura aturada per teclat"


        def insert_data(self):

            try:

               series=[]
               now = datetime.datetime.today()
               pointValues = {
                       "measurement": metric,
                       "fields":{
                             "Power1": self.a,
                             "Power2": self.b,
                         },
                   }

               series.append(pointValues)

               client = InfluxDBClient(host, port, USER, PASSWORD, DBNAME)
               retention_policy = 'awesome_policy'
               client.create_retention_policy(retention_policy, '20w', 3, default=True)
               client.write_points(series, retention_policy=retention_policy)

            except ValueError:
                  print "Error al introduir les dades"

if __name__ == "__main__":

        print " 'Control of electric consumption' "
        c = PowerServer()
        c.read_sensor()
