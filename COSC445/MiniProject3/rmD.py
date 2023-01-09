import pymongo, json, sys

client = pymongo.MongoClient (host='da1') # the gcp instance forwards back to da1
db = client ['fdac22-tags']
tg = db ['tags']

for line in sys.stdin:
 path = line .rstrip()
 tg.remove ({ "path": path })
