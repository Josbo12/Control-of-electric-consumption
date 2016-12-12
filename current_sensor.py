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
metric = "powerdata"


class PowerServer(object):

        def __init__(self):
            super(PowerServer, self).__init__()



        def read_sensor(self):

                try:
                       while True:
                               response = ser.readline()
                               self.z = response.split(",")
                               self.z.pop()
                               self.z = map(float, self.z)


                               for i in range(len(self.z)):
                                   self.z[i]=int(self.z[i])


                               if len(self.z)>=2:
                                   #print "hora %s " % datetime.datetime.today()
                                   #print ("Hora:"+str(datetime.datetime.today())+ "        Power 1: "+str(self.z[0])+
                                   #           " Watts      Power 2: "+str(self.z[1])+"  Watts")
                                   #print "Power 2: %s  Watts" % self.z[1]
                                   self.insert_data()



                except KeyboardInterrupt:
                    print "Lectura aturada per teclat"


        def insert_data(self):

            try:
               series=[]
               now = datetime.datetime.today()
               pointValues = {
                       #"time": now.strftime ("%Y-%m-%d %H:%M:%S"),
                       "measurement": metric,
                       "fields":{
                             "Power1": self.z[0],
                             "Power2": self.z[1],
                         },
                   }

               series.append(pointValues)

               client = InfluxDBClient(host, port, USER, PASSWORD, DBNAME)
               retention_policy = 'awesome_policy'
               client.create_retention_policy(retention_policy, '3d', 3, default=True)
               client.write_points(series, retention_policy=retention_policy)

            except ValueError:
                  print "Error al introduir les dades"

if __name__ == "__main__":

        print " 'Control of electric consumption' "
        c = PowerServer()
        c.read_sensor()
