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

def main():

        host ='localhost'
        port = 8086
        metric = "powerdata"
        series = []


        try:
               while 1:
                       response = ser.readline()
                       z = response.split(",")
                       if len(z)>=2:
                               print "Power 1: %s Watts" % z[0]
                               print "Power 2: %s Watts" % z[1]
                               print "Power 3: %s Watts" % z[2][:-2]

                       pointValues = {
                               "time": now.strftime ("%Y-%m-%d %H:%M:%S"),
                               # "time": int(past_date.strftime('%s')),
                               "measurement": metric,
                               "columns": ["POWER_1","POWER_2","POWER_3"],
                               "fields":  [z[0], z[1], z[2]],
                               "tags": {
                                   "hostName": hostName,
                               },
                           }
                       series.append(pointValues)
                       print(series)

                       client = InfluxDBClient(host, port, USER, PASSWORD, DBNAME)

                       retention_policy = 'awesome_policy'
                       client.create_retention_policy(retention_policy, '3d', 3, default=True)


                       client.write_points(series, retention_policy=retention_policy)

                       time.sleep(10)


        except KeyboardInterrupt:
               ser.close()

if __name__ == '__main__':
        main()
