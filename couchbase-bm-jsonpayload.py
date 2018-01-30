#!/usr/bin/env python

import time, thread, sys, couchbase
from couchbase.cluster import Cluster, PasswordAuthenticator
from random import *

##Global Declarations -
CouchbaseServerAddress = 'couchbase://<ip-address>'
CouchbaseUsername = '<username>'
CouchbasePassword = '<password>'
CouchbaseBucketName = '<bucketname>'

def CbClusterConnect():
    cluster = Cluster(CouchbaseServerAddress)
    cluster.authenticate(PasswordAuthenticator(CouchbaseUsername, CouchbasePassword))
    return cluster
            
def cbkiller( ThreadNumber , StartVal, EndVal):
    MyCluster = CbClusterConnect()
    bucket = MyCluster.open_bucket(CouchbaseBucketName)
    for VALUE in range(StartVal,EndVal):
        JSONKey = 'KEY-'+str(random())
        JSONVal = VALUE
        bucket.upsert(JSONKey, JSONVal, ttl=600, format=couchbase.FMT_JSON)
        print "T# %d - %s : %s " % ( ThreadNumber, JSONKey, str(bucket.get(JSONKey).value) )
        for BCI in range(5,25, 5):
            NewValue = bucket.counter(JSONKey, delta=BCI)
            print "T# %s - new : %d" %( ThreadNumber, NewValue.value)

NumThreads = int(sys.argv[1]) + 1
Doc_Count = int(sys.argv[2])
Sval = 1
Eval = Doc_Count

for COUNT in range(1, NumThreads):
    try:
        thread.start_new_thread( cbkiller, (COUNT, Sval, Eval, ) )
        Sval = Eval + 1
        Eval = Eval + Doc_Count
    except:
        print "Error: unable to start thread"

while 1:
    pass