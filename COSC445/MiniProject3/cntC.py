import pymongo
#client = pymongo.MongoClient () # the gcp instance forwards back to da1
client = pymongo.MongoClient (host='dbNew') # use this instead if running on da0
db = client ['mean-dev']

#"label" : "chopped melon", "cluster_name" : "chopped melon"
print ("|query|cnt|\n|--|--|")

#for l in db.clusters.find ({ "$where": "function() { return this.label != this.cluster_name }" }):
cnt = {}
for l in db.clusters.find ( { "label" : { "$eq" : "other" } }):
  if l['cluster_name'] not in cnt:
    cnt[l['cluster_name']] = 1
  else:
    cnt[l['cluster_name']] += 1

for cn in cnt .keys ():
  print ('|' + cn + '|' + str(cnt[cn]) + '|')
