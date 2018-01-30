#!/usr/bin/env python
import thread
import sys
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

NumThreads = int(sys.argv[1])
Doc_Count = int(sys.argv[2])
Sval = 1
Eval = Doc_Count

for i in range(1, NumThreads):
    try:
        thread.start_new_thread( cbkiller, ("Thread-"+str(i), Sval, Eval, ) )
        Sval = Eval + 1
        Eval = Eval + Doc_Count
    except:
        print "Error: unable to start thread"
    
while 1:
    pass