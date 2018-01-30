#!/usr/bin/env python

import sys
import time
from couchbase.cluster import Cluster, PasswordAuthenticator
import couchbase

def CbClusterConnect():
    cluster = Cluster('couchbase://<server-ip>')
    cluster.authenticate(PasswordAuthenticator('username', 'password'))
    return cluster

def KeepCheck(KeyToCheck):
    MyCluster = CbClusterConnect()
    bucket = MyCluster.open_bucket('<BucketName>')
    CheckCounter = 1
    while True :
        print "Check "+str(CheckCounter)+" : "+bucket.get(KeyToCheck).value
        time.sleep(1)
        CheckCounter += 1
            
def cbkiller( JSONKey , JSONVal):
    MyCluster = CbClusterConnect()
    bucket = MyCluster.open_bucket('<BucketName>')
    bucket.upsert(JSONKey, JSONVal, ttl=600, format=couchbase.FMT_JSON)
    print "Output : "+bucket.get(JSONKey).value
    #KeepCheck(JSONKey)

cbkiller(sys.argv[1], sys.argv[2])