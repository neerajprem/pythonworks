#!/usr/bin/env python

from couchbase.cluster import Cluster, PasswordAuthenticator
from random import *

cluster = Cluster('couchbase://172.31.4.221')
cluster.authenticate(PasswordAuthenticator('admin', 'froggy'))
bucket = cluster.open_bucket('mf-test')

for inc in range(1,1000000):
    CBKEY = 'name'+str(random())
    CBVALUE = 'amazing'+str(inc)
    print CBKEY+' : '+CBVALUE
    bucket.upsert(CBKEY,CBVALUE)
    res = bucket.get(CBKEY)
    print res.value

print "Bye"