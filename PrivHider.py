#!/usr/bin/env python3
"""Simple script for hide information in column in CSV
"""
import csv
import datetime
import os
import base64

ENC = 'ENC**'
PATH = 'C:\\Data\\'
PASSWORD = 'Pa$$w0rd'
COLUMN_HIDE = 0 #Column to hide information


class HidePersonalData():
        def __init__(self, file):
            self.file = file
            self.encrypt = True
            self.decrypt = False

        def str_xor(self, s1, s2):
            return "".join([chr(ord(c1) ^ ord(c2)) for (c1,c2) in zip(s1,s2)])

        def readcsv(self, delim = ';'):
            with open(self.file , 'r') as f:
                r = csv.reader(f, delimiter = delim)
                next(r, None) #skip header

                #r = csv.DictReader(f)
                for row in r:
                    #array = row.split(';')
                    data = row[COLUMN_HIDE]

                    if self.encrypt:
                             data = base64.encodestring(bytes(self.str_xor(data, PASSWORD)))
                             #print(ENC+data)
                    else:
                        if self.decrypt:
                            data = str_xor(PASSWORD, data)
                            #print(data)

                    print(data)



def count_perf(f):
    def wraper(*args, **kwargs):
        time_init = datetime.datetime.now()
        print('Init {}'.format(f.__name__))
        result = f(*args, **kwargs)
        time_end = datetime.datetime.now()
        total = time_end -  time_init
        print('Done. {}'.format(total))
        return 
    return wraper 


#@count_perf
def GetDirFiles(Dir = ''):
    for filename in os.listdir(Dir):
        file = os.path.join(Dir,filename)
        readcsv(file)
        print(file)

        
if __name__=="__main__":
   H = HidePersonalData('C:\\DATA\\1.csv')
   H.readcsv()