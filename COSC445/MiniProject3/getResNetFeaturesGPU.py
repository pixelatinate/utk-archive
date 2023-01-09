import tensorflow as tf 
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.applications.resnet50 import preprocess_input
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, GlobalAveragePooling2D
from tensorflow.keras.models import Model
import sys, os, csv, glob
import pandas as pd
#import numpy as np
import pymongo
from io  import StringIO
from bson.binary import Binary
import json
from bson.objectid import ObjectId


clustering_model = Sequential ()
clustering_model .add (ResNet50(include_top = False, pooling='ave', weights = 'imagenet'))
clustering_model .add (GlobalAveragePooling2D()) # get from 7x7x2048 to 2048
clustering_model .layers[0] .trainable = False
clustering_model .compile (optimizer='sgd', loss='categorical_crossentropy', metrics=['accuracy'])


client = pymongo.MongoClient (host='da1') # the gcp instance forwards back to da1
db = client ['fdac22-tags']
coll = db ['tags']


img_size = 224

missed_imgs = []


for line in sys.stdin:
 (path, cl1, cl2) = line .rstrip(). split(';')
 print (path+';'+cl1+';'+cl2)
 try:
  img = tf.io.read_file("/img/"+path)
  img = tf.io.decode_jpeg(img, channels=3)
  img = tf.image.resize(img, (224,224))


  img1 = tf.keras.applications.resnet50.preprocess_input(tf.expand_dims(img, axis = 0))
  resnet_feature = clustering_model.predict(img1, steps=1)
  fv = pd.Series(resnet_feature.flatten()).to_json(orient='values')

  img1 = tf.image.rot90 (img, -1)
  img1 = tf.keras.applications.resnet50.preprocess_input(tf.expand_dims(img1, axis = 0))
  resnet_feature = clustering_model.predict(img1, steps=1)
  fv1 = pd.Series(resnet_feature.flatten()).to_json(orient='values')

  img1 = tf.image.rot90 (img, 1)
  img1 = tf.keras.applications.resnet50.preprocess_input(tf.expand_dims(img1, axis = 0))
  resnet_feature = clustering_model.predict(img1, steps=1)
  fv2 = pd.Series(resnet_feature.flatten()).to_json(orient='values')
  
  img1 = tf.image.rot90 (img, 2)
  img1 = tf.keras.applications.resnet50.preprocess_input(tf.expand_dims(img1, axis = 0))
  resnet_feature = clustering_model.predict(img1, steps=1)
  fv3 = pd.Series(resnet_feature.flatten()).to_json(orient='values')

  img1 = tf.image.flip_left_right (img)
  img1 = tf.keras.applications.resnet50.preprocess_input(tf.expand_dims(img1, axis = 0))
  resnet_feature = clustering_model.predict(img1, steps=1)
  fv4 = pd.Series(resnet_feature.flatten()).to_json(orient='values')

  img1 = tf.image.flip_up_down(img)
  img1 = tf.keras.applications.resnet50.preprocess_input(tf.expand_dims(img1, axis = 0))
  resnet_feature = clustering_model.predict(img1, steps=1)
  fv5 = pd.Series(resnet_feature.flatten()).to_json(orient='values')
  res2 = coll.insert_one ({'path':path, 'cl1':cl1, 'cl2':cl2, "feature": fv, "feature1": fv1, "feature2": fv2 ,"feature3": fv3, "feature4": fv4,"feature5": fv5 } )
 except Exception as e:
  print (e)
  missed_imgs.append(path)
