#!/usr/bin/env python

import thread
from couchbase.cluster import Cluster, PasswordAuthenticator
from random import *

def cbkiller(ThreadName, StartVal , EndVal):
    cluster = Cluster('couchbase://172.31.4.221')
    cluster.authenticate(PasswordAuthenticator('admin', 'froggy'))
    bucket = cluster.open_bucket('mf-test')
    for inc in range(StartVal,EndVal):
        CBKEY = 'name'+str(random())
        CBVALUE = 'amazing'+str(inc)
        bucket.upsert(CBKEY,CBVALUE)
        res = bucket.get(CBKEY)
        print ThreadName+' -- '+CBKEY+' : '+res.value


for i in range(1, num_of_threads):
    try:
        thread.start_new_thread(cbkiller, ("Thread-"+i, ))
    except:
        print "Error: unable to start thread"

while 1:
       pass

print "Bye"

# try:
#   thread.start_new_thread( cbkiller, ("Thread-1", 1, 1000000, ) )
#   thread.start_new_thread( cbkiller, ("Thread-2", 1000001, 2000000, ) )
#   thread.start_new_thread( cbkiller, ("Thread-3", 2000001, 3000000, ) )
#   thread.start_new_thread( cbkiller, ("Thread-4", 3000001, 4000000, ) )
#   thread.start_new_thread( cbkiller, ("Thread-5", 4000001, 5000000, ) )
#   thread.start_new_thread( cbkiller, ("Thread-6", 5000001, 6000000, ) )
#   thread.start_new_thread( cbkiller, ("Thread-7", 6000001, 7000000, ) )
#   thread.start_new_thread( cbkiller, ("Thread-8", 7000001, 8000000, ) )
#   thread.start_new_thread( cbkiller, ("Thread-9", 8000001, 9000000, ) )
#   thread.start_new_thread( cbkiller, ("Thread-10", 9000001, 10000000, ) )
#   thread.start_new_thread( cbkiller, ("Thread-11", 10000001, 11000000, ) )
#   thread.start_new_thread( cbkiller, ("Thread-12", 11000001, 12000000, ) )
#   thread.start_new_thread( cbkiller, ("Thread-18", 17000001, 18000000, ) )
#   thread.start_new_thread( cbkiller, ("Thread-13", 12000001, 13000000, ) )
#   thread.start_new_thread( cbkiller, ("Thread-14", 13000001, 14000000, ) )
#   thread.start_new_thread( cbkiller, ("Thread-15", 14000001, 15000000, ) )
#   thread.start_new_thread( cbkiller, ("Thread-16", 15000001, 16000000, ) )
#   thread.start_new_thread( cbkiller, ("Thread-17", 16000001, 17000000, ) )
#   thread.start_new_thread( cbkiller, ("Thread-19", 18000001, 19000000, ) )
#   thread.start_new_thread( cbkiller, ("Thread-20", 19000001, 20000000, ) ) 