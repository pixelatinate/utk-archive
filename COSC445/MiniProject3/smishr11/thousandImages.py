import pymongo
from apiclient.discovery import build

myNetID='smishr11'
mySE='a7a4c9ae157e39a6b'
myAPIKey='AIzaSyCOFigLErKietRKppPhX_qJkJpyo6gXWW0'

myQueries=['rotten Strawberries','fresh Tomatillos', 'moldy Tomatillos', 'rotten Tomatillos', 'fresh Tomatoes', 'moldy Tomatoes', 'rotten Tomatoes']


client = pymongo.MongoClient (host='da1') # if you run on da2
# client = pymongo.MongoClient ()      # the gcp instance forwards back to da1
db = client ['fdac22mp3']       # database for mp3
coll = db [myNetID]

service = build("customsearch", "v1",
               developerKey=myAPIKey)

for myQuery in myQueries:
  n=1
  while (n < 10):
    res = service.cse().list(
      q=myQuery,
      cx=mySE,
      searchType='image',
      start=n,
      imgType='photo',
      rights='cc_publicdomain',
      safe='medium'
    ).execute()

    if not 'items' in res:
      print ('No result !!\nres is: {}'.format(res))
      break
    else:
      for item in res['items']:
        n+=1
        try:
          coll.insert_one ( { 'query':myQuery, 'res':item } )
          print(item['title'].encode('ascii', errors='ignore').decode('ascii', errors='ignore') + item['link'])
        except e:
          print ("exception")
