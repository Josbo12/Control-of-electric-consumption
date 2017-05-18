#!/usr/bin/python
# -*- coding: utf-8 -*-


from influxdb import InfluxDBClient
from influxdb.client import InfluxDBClientError
import datetime
import random
import time
from ast import literal_eval
from tk_current_sensor import PowerServer



class Database(object):

        def __init__(self):
            super(Database, self).__init__()


            self.powerserver = PowerServer()
            self.USER = 'root'
            self.PASSWORD = 'root'
            #ser = serial.Serial('/dev/ttyAMA0', 38400, timeout=1)
            self.host ='localhost'
            self.port = 8086
            self.client = InfluxDBClient(self.host, self.port, self.USER, self.PASSWORD)




        def create_database(self, dbname):

             self.DBNAME = dbname
             self.client.create_database(self.DBNAME)

        def insert_data(self):

                   self.powerserver.read_sensor()
                   metric = "mesures"

                   series=[]
                   now = datetime.datetime.today()
                   pointValues = {
                           "measurement": metric,
                           "fields":{
                                 "Pinça 1": self.powerserver.a,
                                 "Pinça 2": self.powerserver.b,
                                 "Pinça 3": self.powerserver.c
                             },
                       }

                   series.append(pointValues)

                   self.client = InfluxDBClient(self.host, self.port, self.USER, self.PASSWORD, self.DBNAME)
                   retention_policy = 'awesome_policy'
                   self.client.create_retention_policy(retention_policy, '20w', 3, default=True)
                   self.client.write_points(series, retention_policy=retention_policy)




        def get_database(self):

            self.llista_databases = []
            dbs = self.client.get_list_database()
            for x in dbs:
                for key, value in x.iteritems():
                    temp = [value]

                ep = u", ".join(temp)

                self.llista_databases.append(ep)






if __name__ == "__main__":

        print " 'Control of electric consumption' "
        c = Database()
        c.create_database()
