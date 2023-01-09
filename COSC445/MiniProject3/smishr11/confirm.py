import pymongo
# client = pymongo.MongoClient () # the gcp instance forwards back to da1
client = pymongo.MongoClient (host="da1") # on da2 docker container
db = client ['fdac22mp3']       # database for mp3
coll = db ['smishr11']
print (coll.count_documents({}))