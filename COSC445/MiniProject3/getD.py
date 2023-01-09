import pymongo, json, sys


client = pymongo.MongoClient (host='da1') # the gcp instance forwards back to da1
db = client ['fdac22-tags']
tg = db ['tags']

for r in tg .find ():
  if 'cl1' in r:
    for k in ('feature', 'feature1', 'feature2','feature3','feature4','feature5'):
      a = json.loads(r[k])
      sys.stdout.write (r['cl1']+';'+r['cl2']+';'+r['path'])
      for v in a: sys.stdout.write(';'+str(v))
      sys.stdout.write('\n')
