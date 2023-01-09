import pymongo,sys

#client = pymongo.MongoClient () # the gcp instance forwards back to da1
client = pymongo.MongoClient ('da1') # use this instead if running on da0
db = client ['fdac22mp3']


items = {};
for l in db.list_collection_names():
 coll = db [l]
 for item in coll.find():
  key = 'res'
  if key not in item: key = 'result' 
  if key in item: 
   title = ''
   if 'title' in item[key]: title = item[key]['title']
   if 'query' in item:
    items [item[key]['link']] = item['query'] + ';' + title
   else: sys.stderr.write(str(item)+"\n")
  else: sys.stderr.write(str(item)+"\n")

for l in items.keys():
 print (l+';'+items[l].encode('ascii', errors='ignore').decode('ascii', errors='ignore'))
