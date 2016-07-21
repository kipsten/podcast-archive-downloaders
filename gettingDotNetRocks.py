import json
import urllib2
import os.path


firstPodcastToDownload = 4
lastPodcastToDownload = 5

downloadFolder = "D:/podcasts/dotnetrocks/"

data = {"Page":1,"PageSize":10000,"SearchString":""}

req = urllib2.Request("https://www.dotnetrocks.com/api/shows-paged-post")
req.add_header('Content-Type', 'application/json')

response = urllib2.urlopen(req, json.dumps(data)).read()

responseJSON = json.loads(response)

responseJSON.reverse()

nItems = len(responseJSON)


for i in range(firstPodcastToDownload-1, lastPodcastToDownload):
    url =  responseJSON[i]["DownloadUrl"]
    showId =  responseJSON[i]["ShowID"]
    title = responseJSON[i]["ShowTitle"].encode('ascii','ignore')

    fileName = "rocks--" + str(showId) + "--" + title + ".mp3"
    fullFilePath = downloadFolder + fileName;

    if os.path.isfile(fullFilePath):
        print "already exists"
        continue

    mp3file = urllib2.urlopen(url)
    with open(fullFilePath,'wb') as output:
      output.write(mp3file.read())
