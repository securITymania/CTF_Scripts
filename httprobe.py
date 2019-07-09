#This script is used to detect the domain is accepting HTTP or HTTPS connection
#You can pass Sub-domaina list as input
#Bugbounty collection script

import requests
from urlparse import urlparse
from threading import Thread
import urllib2
import sys
from Queue import Queue

concurrent = 200
def help_msg():
    msg = """-h  for help\n Usage: python httprobe.py doamins_list.txt
    """
    print(msg)

def doWork():
   while True:
       url = q.get()
       url = getStatus(url)
       doSomethingWithResult(url)
       q.task_done()

def getStatus(ourl):
   try:
       res = requests.get("http://"+ourl)
       return res.url
   except:
       return "error", ourl

def doSomethingWithResult(url):
   print(url)

q = Queue(concurrent * 2)
for i in range(concurrent):
   t = Thread(target=doWork)
   t.daemon = True
   t.start()
try:
    if sys.argv[1] =="-h":
        help_msg()
    else:
        for url in open(sys.argv[1],'r'):
           q.put(url.strip())
        q.join()
except KeyboardInterrupt:
   sys.exit(1)
