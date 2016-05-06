from sh import youtubeApi as yt
import simplejson as json

class YoutubeTalker:
    def __init__(self):
        self.listOfItems={}
        self.storedFile='.videos_list'

    def LoadVideosInfoFromFile(self):
        with open(self.storedFile, 'r') as f:
            self.listOfItems=json.load(f)
        return {'lastPlayed': self.listOfItems}

    def SaveInformationAboutVideo(self, videoId):
        if videoId not in self.listOfItems:
            data_from_api= self.getInfoFromApi(videoId)
            with open(self.storedFile) as f:
                try:
                    data= json.load(f)
                    data.update(data_from_api)
                    print(data)
                except:
                    data = data_from_api
            with open(self.storedFile, 'w') as f:
                json.dump(data, f, sort_keys= True, indent= 2, ensure_ascii=False)
            return {'result': 'OK', 'message':'Made call to Youtube API. Stored new data in file'}
        else:
            return {'result': 'OK', 'message':'Not saved, because video is on list already'}

    def getInfoFromApi(self, videoId):
        ytOutput= yt(videoId)
        print("ytOutput:")
        print(ytOutput)
        data= json.loads(ytOutput.stdout)
        to_return={}
        for item in data["items"]:
            to_return[item["id"]]= {'id': item["id"], 'title': item['snippet']["title"], 'thumbnail': item['snippet']["thumbnails"]["default"]["url"]}
        print(to_return)
        return to_return

