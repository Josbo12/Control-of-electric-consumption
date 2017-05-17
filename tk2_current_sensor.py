#!/usr/bin/python
from influxdb import InfluxDBClient
from influxdb.client import InfluxDBClientError
import datetime
import random
import time
#import serial



USER = 'root'
PASSWORD = 'root'


#ser = serial.Serial('/dev/ttyAMA0', 38400, timeout=1)
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
            self.client = InfluxDBClient(host, port, USER, PASSWORD)



        def read_sensor(self):

                try:
                       #while True:
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
                               self.insert_data()



                except KeyboardInterrupt:
                    print "Lectura aturada per teclat"



        def create_database(self, dbname):

             self.DBNAME = dbname
             self.client.create_database(self.DBNAME)

        def insert_data(self):

            try:
               series=[]
               now = datetime.datetime.today()
               pointValues = {
                       "measurement": metric,
                       "fields":{
                             "Power1": self.a,
                             "Power2": self.b,
                             "Power2": self.c
                         },
                   }

               series.append(pointValues)

               self.client = InfluxDBClient(host, port, USER, PASSWORD, self.DBNAME)
               retention_policy = 'awesome_policy'
               self.client.create_retention_policy(retention_policy, '20w', 3, default=True)
               self.client.write_points(series, retention_policy=retention_policy)

            except ValueError:
                  print "Error al introduir les dades"


        def get_database(self):

            self.llista_databases = []
            dbs = self.client.get_list_database()
            print dbs
            print type(dbs)
            print type(dbs[0])
            b = dbs[0]
            for x in dbs:
                for key, value in x.iteritems():
                    temp = [value]
                #print temp
                ep = u", ".join(temp)
                #print ep
                self.llista_databases.append(ep)

if __name__ == "__main__":

        print " 'Control of electric consumption' "
        c = PowerServer()
        c.read_sensor()
