## MP3 Part A: Due Oct 18 at the end of the class

# Data Retrieval  and Storage

The task described here is not a futile exercise focused exclusively on
increasing your skills at the task of large-scale data retrieval.
It also represents an actual research objective of creating a very large
dataset of labeled images: a common task for contemporary
deep-learning-related research that requires large labeled datasets
to train these models.

## Part A: find and store metadata


We will use GCP Custom Search API to complete this task.
Each of you will get a search string and will use the CS API to
retrieve and store 1000 images in the MongoDB. You may
use GCP instance to accomplish this task.

You might not get the 1000 records using the assigned search
strings. If so, please invent your own object with the decay-level
adjectives to complete the collection. I will be looking to get 1000
records in your collection.

The ten search strings assigned to you
[can be found here](https://github.com/fdac22/Miniproject3/blob/master/queries.md) 

Some
[initial setup](https://rayxyz.github.io/tech/2018/05/16/setup-google-custom-search-and-search-images-using-python.html)
is necessary in order to use GCP CS API.

Specifically, log in to your google account (where gcp credits are applied) then go to your GCP console
https://console.cloud.google.com/apis/dashboard
(make sure the project is the one you selected for GCP)
and click on "Enable APIs and Services" and search for Custom
and select Custom Search API and enable it.

then go to 
[create custom search engine](https://cse.google.com/cse/create/new)
enter any site and then click on "Control Panel" next to 
"Modify your search engine"

Select "Image Search on", and "Search the entire web on"


Then copy "Search engine ID", to be used as the cx parameter
below. 


Now get credentials:
https://console.developers.google.com/apis/credentials

select the right project, create credentials (select API key).

The resulting key will be used below. 


Please note some differences from the instructions on the page:
```
sudo pip install --upgrade google-api-python-client
```



Below is python code you can adapt for your task, please
debug first with a single iteration (and single query),
before retrieving all 1000 images.

```
import pymongo
from apiclient.discovery import build

myNetID='YourNetID'
mySE='YourSearchEngine'
myAPIKey='YourAPIKey'

myQueries=['YourQuery1', 'YourQuery2', ..., 'YourQuery10']


client = pymongo.MongoClient (host='da1') # if you run on da2
# client = pymongo.MongoClient ()      # the gcp instance forwards back to da1
db = client ['fdac22mp3']       # database for mp3
coll = db [myNetID]

service = build("customsearch", "v1",
               developerKey=myAPIKey)

for myQuery in myQueries:
  n=1
  while (n < 100):
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
```

If you put the above code in a python file (or notebook) and run it, it should populate
the database. Once that is done, you can check the number of images in your collection via
```
# client = pymongo.MongoClient () # the gcp instance forwards back to da1
client = pymongo.MongoClient (host="da1") # on da2 docker container
db = client ['fdac22mp3']       # database for mp3
coll = db ['myNetID']
print (coll.count())
```

# Part B: Due Oct 27 end of day

Find a video of rotting/evolving objects and extract frames coresponding to diffreent levels of decomposition.

This channel may be a good start: https://www.youtube.com/playlist?list=PL0FB8D619E5C752AE

For example: 

 - Apple: https://www.youtube.com/watch?v=ajay1tq_roU&ab_channel=TemponautTimelapse
 - Bananas: https://www.youtube.com/watch?v=ERgCeui5bp4&ab_channel=TemponautTimelapse
 - Mango: https://www.youtube.com/watch?v=NzAYAcneGmY&ab_channel=TemponautTimelapse
 - Peach: https://www.youtube.com/watch?v=g9pf19wk0-E&ab_channel=TemponautTimelapse
 - Cucumber: https://www.youtube.com/watch?v=Q0TSsRtctEQ&ab_channel=TemponautTimelapse
 - Tomatoes: https://www.youtube.com/watch?v=xP3swUFkwoU&ab_channel=TemponautTimelapse
 - Flower: https://www.youtube.com/watch?v=I8W4LyIXINE&list=WL&index=40&ab_channel=NationalGeographic

Step 1. Please select one video preferably depicting the decaty of the fruit/vegatable that you had been assigned in Part A. If you can find no such videos, select an object that you find of interest.

Step 2: To download mp4 video do, for example:

    1. Visit https://offeo.com/free/youtube-to-mp4/ or https://www.kapwing.com
    1. Copy and paste youtube video link into download bar
    1. Download the mp4 version of the video: also, check out https://github.com/ytdl-org/youtube-dl <- good terminal application for downloading media content. 

Step 4: Pick and extract at least two frames for each stage of the decomposition:

    - fresh
    - rotten
    - moldy (if applicable)

   How to extract frames using OpenCV:
```
import cv2
vid = cv2 .VideoCapture('YourVideo.mp4')
success, img = vid .read()
count = 0
while success:
  if count % 100 == 0: # write one out of 100 frames
    cv2 .imwrite ("YourVideoFrame.%d.jpg" % count, img)      
  success, img = vid .read()
  print ('Read frame: ', success)
  count += 1
```

cv2 is not installled in the docker container:
in the terminal please type:
```
sudo apt update
sudo apt install python3-opencv
```
if you are installing without root access
```
pip3 install --user opencv-python
```

After installing please do kernel -> restart on your notebook 

Please store/process on da2 in your home folder




Step 5: Rename the frames using the object depicted and stage of the decomposition: 
   yourutkid.Object.stage.frame#.png
   

  
# Part C Due Nov 8

The search often retrieves irrelevant images. This task in part C is to identify correct images so that the 
data used to train CNN models in part D is accurate.


Each one is assigned a number of search terms (clusters) to equalize the number
of images for each of you to review. The specific clustersi are in
[clusters.md](https://github.com/fdac22/Miniproject3/blob/master/clusters.md)

To do that please login to a specialized container:

- ssh -p3099 -L3000:localhost:3000 yourNetID@da0.eecs.utk.edu

- go to your browser url http://localhost:3000/

- sign up with your utkid/arbitrary password(please write it down)

- select tabb clusters/browse clusters

- select (one by one) each of your clusters (see below)

- for each image (in each of your clusters) select the correct label (choose "other" if no label is accurate)

- check if you made modifications to a cluster using the following
code on the terminal (the one you got via ssh -p3099 -L3000:localhost:3000 yourNetID@da0.eecs.utk.edu
```
cd Miniproject3
python3 cntC.py
```

If you see your cluster, that means editing was done.

The output will be stored in 
[statusC.md](https://github.com/fdac22/Miniproject3/blob/master/statusC.md)

Some of the images do not show up or do not match any category: mark these as "other"


# Part D Due Nov 15

I will show how to calculate the deep network (ResNet50) features for each
labeled image. [What is Neural Network?](https://victorzhou.com/blog/intro-to-neural-networks); 
What is [CNN: Convolutional Neural Network?](https://victorzhou.com/blog/intro-to-cnns-part-1);
How to use [Keras](https://victorzhou.com/blog/keras-neural-network-tutorial) to fit CNNs?

## Please don't run these steps as the server will not be able to handle that!

We will then explore the features obtained by the
entire class. Below I illustrate how to detect if the
vegetable/fruit is decayed and if we can recognize which fruit is
depicted in the photo.

The very first step is to clean up the data, especially different capitalization of keywords. 
```
python3 listC.py | sed 's|.*/fruit_img/||' | lsort 1G -t\; -u > listC
```

Then calculate the features from the images (I am running audris/keras docker image as it has the right software preinstalled:

```
cat process |  while IFS=\; read p c1 c2; do python getResNetFeatures1.py /data/img/$p $utid $c1 $c2; done
```

This may take several hours of compute time, so it is best to run it inside tmux.


The following command taks what has be processed so far out of the database

```
python3 getD.py | gzip > features.gz
```

This output will keep changing as more of you process images as
getD.py captures features from all images, not just ones you
have processed. 


Next we read the features into R:
```
R --no-save
library(randomForest)
library(caret)
dat=read.table("features.gz", sep=";")
names(dat)=c("state","fruit","path", paste("f", 1:2048, sep=""))
```

Follow next steps in Analysis.ipynb

### Individual assignments

Fit a classification model and report confusion matrix for predictin a 
specific outcome specified below.
To be precise, you do binary classification with the the response variable being the combination specified. 
For example, the response for TBD is:
```
Y = dat$state=="fresh"&dat$fruit=="kale"
```
You are welcome to use classification methods that are provided here
or any other methods. You need to provide the code 
in Analysis.ipynb or Analysis.md in your fork of MP3 and resubmit the pull request.
To speed up your modeling process I have prepared
AnalysisTemplate.ipynb and on docker container created features.csv
file for each of you. Please use it instead of the full features.gz
as shown in the template. The full file takes 20min just to read
into R. 


|utid|state|object|
|----|-----|------|
|ababjac|fresh|mushrooms |
|abahour2|fresh|corn |
|abrock14|fresh|grapes |
|acook46|fresh|apples |
|ahillhou|rotten|tomatoes |
|awelden2|fresh|strawberries |
|clee95|fresh|blackberries |
|cwang93|fresh|basil |
|dscott57|fresh|carrots |
|jblanch8|rotten|parsley |
|jclar168|fresh|beets |
|jim5|fresh|potatoes |
|jmandzak|rotten|strawberries |
|jrodeghi|fresh|melons |
|jsadik|rotten|corn |
|jstaman|fresh|raspberries |
|kmaclin1|fresh|green_onions |
|ljakstas|fresh|guava |
|lsharpe8|fresh|peaches |
|lwrinkle|fresh|garlic |
|mdeleon1|fresh|artichokes |
|mdenise|rotten|mushrooms |
|npatel79|moldy|strawberries |
|pbowlin1|fresh|grapefruits |
|rseamons|fresh|avocados |
|rsexton8|rotten|raspberries |
|smishr11|rotten|summer_squash |
|spunjani|fresh|pineapples |
|tainley|fresh|figs |
|tcultice|fresh|cherries |
|troger28|fresh|okra |
|wparham1|fresh|blueberries |
|zmalkmus|moldy|summer_squash |
|rwill166|fresh|green_peas |
|beken|rotten|green_onions |
|bkammerd|fresh|bread |
|chagens|fresh|asparagus |
|cjohn260|rotten|tomatillos |
|delzinga|rotten|nectarines |
|dhuang14|rotten|fiddleheads |
|elidberb|rotten|collards |
|lpearcy1|moldy|nettles |
|rschenck|fresh|salsify |
|sblank11|fresh|plums |
|spate118|rotten|grapes |
|tkhan7|fresh|pears |
|gkirk|fresh|eggplant |
|mduraney|fresh|apricots |
|yahmad1|rotten|garlic |
|amcdan23|fresh|collards |
|batkhamj|fresh|quinces |
|cbrook53|fresh|cucumber |
|dseals3|fresh|morels |
|klee50|fresh|nettles |
|sjohn248|rotten|figs |
|cbeckfor|fresh|oranges |
|dwill148|fresh|green beans|
|pattle|rotten|nettles |
|tneuefei|fresh|pea_beans |
|awalsh15|fresh|passionfruit |
|bmclaug6|fresh|cauliflower |
|cbrow216|fresh|carambola |
|rpatel77|rotten|tangelos |
|vhazlewo|rotten|grapefruits |
|echavez2|fresh|tangerines |
|ntayefeh|moldy|raspberries |
|friya|fresh|rhubarb |
|aartates|fresh|lettuce |
|bgullet1|fresh|kale |
|bschwar7|rotten|carrots |
|dwhite75|fresh|spinach |
|hhaynie|fresh|limes |
|relgedaw|fresh|cherimoyas |
|robdgrif|rotten|plums |
|shoque|rotten|endive |
|tharshba|rotten|broccoli |
|tnitzsch|fresh|lemongrass |
|zlim2|fresh|brussels sprouts|
|aesser|rotten|lettuce |
|eander68|fresh|kiwi |
|aenzor|rotten|potatoes |
|aphan2|rotten|mustard |
|bbutle11|fresh|navel_oranges |
|broachel|fresh|cranberries |
|hfarahat|fresh|parsnips |
|imulet|fresh|celery |
|jamin|fresh|tomatoes |
|jsun36|fresh|kohlrabi |
|kyumhan|fresh|fiddleheads |
|nmize1|bad|cucumber |
|oameli|rotten|tangerines |
|rswan|rotten|morels |
|vbhupati|rotten|kumquats |
|vhanset|rotten|black-eyed_peas |
|whannon1|moldy|navel oranges|
|zhamm|fresh|medjool_dates |
|zhayes2|rotten|navel_oranges |
|cearhear|rotten|watercress |
|csmit402|rotten|asparagus |
|jallbrit|fresh|radish |
|zwilli13|fresh|persimmons |
|ahickm18|fresh|peppers |
|lgangula|fresh|arugula |
|ssuresh6|fresh|chili_pepper |
|jmuncy2|rotten|boysenberries |




# Useful tools

Working with servers it is always worth using terminal emulator. It, for example, 
keeps track of running process or connections to other servers while you may disconnect from it from your laptop.

One such emulator is tmux. Simply start it once connected to the container via
```
tmux
```

Once it starts, you can simply close the terminal: the processes within it will continue. 
Once you log in again you can reconnect via
```
tmux a
```
(a stands for attach). 
You can also create additional windows via <ctrl>-b c, disconnect via <ctrl>-b d, switch to next window <ctrl>-b n, etc. Look for tmux cheat-sheet in web search for more info. 
  
 







