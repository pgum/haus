from sh import youtubeApi as yt

class YoutubeTalker:
    def __init__(self):
        self.listOfItems=[]
        self.storedFile='.videos_list'

    def LoadVideosInfoFromFile(self):
        with open(self.storedFile, 'r') as f:
            self.listOfItems=json.load(f)
        return {'lastPlayed': self.listOfItems}

    def SaveInformationAboutVideo(self, videoId):
        if videoId not in self.listOfItems:
            with open(self.storedFile, 'a') as f:
                json.dump(getInfoFromApi(videoId), f, sort_keys= True, indent= 2, ensure_ascii=False)
            return {'result': 'OK', 'message':'Made call to Youtube API. Stored new data in file'}

    def getInfoFromApi(self, videoId):
        data= json.loads(yt(videoId))
        to_return={}
        for item in data["items"]:
            to_return[item["id"]= {'title': item['snippet']["title"], 'thumbnail': item['snippet']["thumbnails"]["default"]["url"]
        return to_return;

