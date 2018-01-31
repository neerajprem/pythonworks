#!/usr/bin/env python

import time, thread, sys, couchbase
from couchbase.cluster import Cluster, PasswordAuthenticator
from random import *

##Global Declarations -
CouchbaseServerAddress = 'couchbase://172.31.15.171'
CouchbaseUsername = 'admin'
CouchbasePassword = 'froggy'
CouchbaseBucketName = 'mfl-test'
KeyExpireTime = 600

def CbClusterConnect():
    cluster = Cluster(CouchbaseServerAddress)
    cluster.authenticate(PasswordAuthenticator(CouchbaseUsername, CouchbasePassword))
    return cluster
            
def cbkiller( ThreadNumber , StartVal, EndVal):
    MyCluster = CbClusterConnect()
    bucket = MyCluster.open_bucket(CouchbaseBucketName)
    while True :
        for VALUE in range(StartVal,EndVal):
            JSONKey = 'KEY-'+str(random())
            JSONVal = VALUE
            bucket.upsert(JSONKey, { "MOONFROG-"+str(JSONVal) : { JSONKey+"amazingvalue" : str( JSONVal*0.9)+"ThisMakesMagic" }, "ADDRESS" : { "Locality":"Cambridge Layout", "Area":"Indiranagar", "Pincode": 560043 }, "Employees" : "100-200", "WEBSITE" : "www.moonfroglabs.com", "CONTACT" : "9986239645", "DEPARTMENTS" : { "DevOps" : { "KeyPerson 1 " : "Neeraj Prem Verma" , "KeyPerson 2" : "Gaurav Tayal"}, "Account" : { "KeyPerson 1 " : "Ashwini Khemka" , "KeyPerson 2" : "Chetan Kejriwal"}, "Human Resource" : { "KeyPerson 1 " : "Deepa Naidu", "KeyPerson 2" : "Surabhi Aswal", "KeyPerson 3" : "Varsha Sharma", "KeyPerson 4" : "Samhita", "KeyPerson 5" : "Adarsh", "KeyPerson 6" : "Navjot Poddar", "Site Reliability Engineering" : { "KeyPerson 1 " : "Mohammad Shafin", "KeyPerson 2" : "Denis DSouza", "KeyPerson 3" : "Koushik Paul" } } } } , ttl = KeyExpireTime, format=couchbase.FMT_JSON)
            print "T# %d - %s : %s " % ( ThreadNumber, JSONKey, str(bucket.get(JSONKey).value) )
        time.sleep(20)
    print "cbkiller over" 

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