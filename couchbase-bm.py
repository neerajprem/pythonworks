#!/usr/bin/env python
import thread
import sys
from couchbase.cluster import Cluster, PasswordAuthenticator
from random import *

CouchbaseServerAddress = 'couchbase://172.31.15.171'
CouchbaseUsername = 'admin'
CouchbasePassword = 'froggy'
CouchbaseBucketName = 'mfl-test'
KeyExpireTime = 600

def cbkiller(ThreadName, StartVal , EndVal):
    cluster = Cluster(CouchbaseServerAddress)
    cluster.authenticate(PasswordAuthenticator(CouchbaseUsername, CouchbasePassword))
    bucket = cluster.open_bucket(CouchbaseBucketName)
    for inc in range(StartVal,EndVal):
        CBKEY = 'name'+str(random())
        CBVALUE = 'amazing'+str(inc)
        bucket.upsert(CBKEY,CBVALUE, KeyExpireTime)
        res = bucket.get(CBKEY)
        print ThreadName+' -- '+CBKEY+' : '+res.value

NumThreads = int(sys.argv[1]) + 1
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