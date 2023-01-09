import pymongo
from pymongo import MongoClient
from datetime import datetime
import sys

client = MongoClient("dbNew")
db = client.get_database("mean-dev")

data = sys.stdin.readlines()
for img in data:
    now = datetime.now()
    image = "/"
    path = img.split(";")[0].strip().split("/")[-3:]
    print (path)
    label = img.split(";")[1].strip()
    path[0]='localhost:3000'
    image = '/' + "/"+image.join(path)
    #print ({ "image" : image,   "label" : label, "cluster_name": label,    "created" : now,  "__v" : 0  })
    try:
      db.clusters.insert({ "image" : image,   "label" : label, "cluster_name": label,    "created" : now,  "__v" : 0  })
    except:
      print ("bad")
