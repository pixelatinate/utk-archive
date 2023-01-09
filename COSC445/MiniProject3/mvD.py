import pymongo, json, sys

client = pymongo.MongoClient (host='da1') # the gcp instance forwards back to da1
db = client ['fdac22-tags']
tg = db ['tags']

for line in sys.stdin:
 (path, clo0, clo1, cln0, cln1) = line .rstrip().split(';')
 tg.update_one({ "path": path }, { '$set': { 'cl1': cln0, 'cl2': cln1} }, upsert=False)
