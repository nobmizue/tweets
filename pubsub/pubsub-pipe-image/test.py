#!/usr/bin/env python

#-*- coding:utf-8 -*-
 
import codecs, simplejson, time
 
from tweepy.streaming import StreamListener, Stream
from tweepy.auth import OAuthHandler
from tweepy.api import API
from datetime import timedelta
 
def get_oauth():
    consumer_key = "cJXMUBcenymJSgUPfnyHYVBqd"
    consumer_secret = "JZbjCP6MzUnWLOoU6K2VouCpacmCwvYLmyXMY6wZzR6MyepvsN"
    access_key = "46786366-3BrGV7f5vOXlLMMhrPG32Y3tIQBJ14qiG5rnNVDPo"
    access_secret = "CMOZ61hlhuvDsddbeiYC9Qi34vXkrvyJhZa1v2AFrD3UK"
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    return auth
 
class AbstractedlyListener(StreamListener):
    def on_status(self, status):
        status.created_at += timedelta(hours=9)
        text = status.text
         
        print "-------------------\n"
        print "tweet " + str(status.created_at) +"\n"
        print text + "\n"
 
if __name__ == '__main__':
    auth = get_oauth()
    stream = Stream(auth, AbstractedlyListener(), secure=True)
#    stream.filter(track=["AKB"])
    stream.filter(track=['bigdata', 'kubernetes', 'bigquery', 'docker', 'google',
                       'googlecloud', 'golang', 'dataflow',
                       'containers', 'appengine', 'gcp', 'compute',
                       'scalability', 'gigaom', 'news', 'tech', 'apple',
                       'amazon', 'cluster', 'distributed', 'computing',
                       'cloud', 'android', 'mobile', 'ios', 'iphone',
                       'python', 'recode', 'techcrunch', 'timoreilly']
                )
