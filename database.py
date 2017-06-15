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

            #Parametres oer defecte que definim a la base de dades
            self.powerserver = PowerServer()
            self.USER = 'root'
            self.PASSWORD = 'root'
            self.host ='localhost'
            self.port = 8086
            self.client = InfluxDBClient(self.host, self.port, self.USER, self.PASSWORD)


        def create_database(self, dbname):

            #Creem base de dades amb el nom que ens passa la funció
            self.DBNAME = dbname
            self.client.create_database(self.DBNAME)

        def insert_data(self):

                   #lectura del sensor
                   self.powerserver.read_sensor()

                   #Introduim les lectures a la base de dades
                   metric = "mesures"

                   series=[]
                   now = datetime.datetime.today()
                   pointValues = {
                           "measurement": metric,
                           "fields":{
                                 "Pinça 1": self.powerserver.z[0],
                                 "Pinça 2": self.powerserver.z[1],
                                 "Pinça 3": self.powerserver.z[2]
                             },
                       }

                   series.append(pointValues)

                   self.client = InfluxDBClient(self.host, self.port, self.USER, self.PASSWORD, self.DBNAME)
                   retention_policy = 'awesome_policy'
                   self.client.create_retention_policy(retention_policy, '20w', 3, default=True)
                   self.client.write_points(series, retention_policy=retention_policy)


        def get_database(self):

            #funció per obtenir les bases de dades guardades
            self.list_databases = []
            dbs = self.client.get_list_database()

            #el que ens retorna la funció ho posem en una llista i separat
            for x in dbs:
                for key, value in x.iteritems():
                    temp = [value]

                data = u", ".join(temp)

                self.list_databases.append(data)


if __name__ == "__main__":

        print " 'Control of electric consumption' "
        c = Database()
        c.create_database()
