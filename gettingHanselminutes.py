import urllib2
import json
from bs4 import BeautifulSoup
import os.path
import fileinput
import grequests
import operator


folder = "D:/podcasts/Hanselminutes"

# 1-indexed
firstPodcastToDownload = 7
lastPodcastToDownload = 8
numPodcastsToDownload = lastPodcastToDownload - firstPodcastToDownload + 1


lines = []

allText = urllib2.urlopen("http://hanselminutes.com/archives").read()

soup = BeautifulSoup(allText, "lxml")
links = soup.find_all("a" )
episodeLinks = []
for link in links:
    if link.has_attr("class"):
        if link["class"] == ["showCard"]:
            pieces = link["href"].split("/")
            episodeNumber = pieces[1]
            episodeName = pieces[2]
            lines.append( { "episodeNumber":episodeNumber, "episodeName": episodeName} )



lines.reverse()
lines = lines[ firstPodcastToDownload-1 : lastPodcastToDownload]

for line in lines:
    print line
    episodeNumber = line["episodeNumber"]
    episodeName = line["episodeName"]
    
    filename = episodeNumber + "--" + episodeName + ".mp3"
    fullFilePath = folder + filename
    if os.path.isfile(fullFilePath):
        continue
    
    leftPaddedEpisodeNumber = "0" + ("0" * (3-len(str(episodeNumber))) ) + episodeNumber
    # example: "https://s3.amazonaws.com/hanselminutes/hanselminutes_0002.mp3"
    url = "https://s3.amazonaws.com/hanselminutes/hanselminutes_" + leftPaddedEpisodeNumber + ".mp3"
    
    mp3file = urllib2.urlopen(url)
    with open(fullFilePath,'wb') as output:
      output.write(mp3file.read())
    
    
    
    


















