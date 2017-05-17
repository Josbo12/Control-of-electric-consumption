#!/usr/bin/python
# -*- coding: utf-8 -*-


from influxdb import InfluxDBClient
from influxdb.client import InfluxDBClientError
import datetime
import random
import time
from ast import literal_eval


class Database(object):

        def __init__(self):
            super(Database, self).__init__()

            self.USER = 'root'
            self.PASSWORD = 'root'
            #ser = serial.Serial('/dev/ttyAMA0', 38400, timeout=1)
            self.host ='localhost'
            self.port = 8086
            self.client = InfluxDBClient(self.host, self.port, self.USER, self.PASSWORD)


        def create_database(self, dbname):


             self.client.create_database(dbname)

        def insert_data(self):
            try:
                   series=[]
                   now = datetime.datetime.today()
                   pointValues = {
                           "measurement": metric,
                           "fields":{
                                 "Pinça 1": self.a,
                                 "Pinça 2": self.b,
                                 "Pinça 2": self.c
                             },
                       }

                   series.append(pointValues)


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
        c = Database()
        c.create_database()
