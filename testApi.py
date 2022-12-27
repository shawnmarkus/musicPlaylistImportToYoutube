from flask import Flask , request
from flask_restful import Resource,Api
from urllib.parse import urlparse

# import file for using the dedicated function
from ressoMusicList import fetchRessoPlayList
from youtubeFetch import fetchYoutubePlayList
from createListOfIdForVideos import searchAndAddToListOnYoutube
from makeCallToCreateAndListAppend import createPlaylistOnYouTube
from spotifyExtractDetail import fetchPlaylistDetail


app = Flask(__name__)
api = Api(app)



class HelloWorld(Resource):
    def __init__(self):
        pass

    
    def get(self):
        # start
        url_provided = request.get_json()["url"]
        parse_object = urlparse(url_provided)
        # print(url_provided)
        Platform = parse_object.netloc
        # return {f"Platform": Platform}
        # arr = Platform.split(".")
        # actualName = arr[1]
        # if actualName =="youtube":
        #     return {"Platform": actualName}
        # elif actualName == "resso":
        #     return {"Platform": actualName}
        # elif actualName == "spotify":
        #     return {"Platform": actualName}
        # # end
        # return {"Note":f"Platform choosen is '{actualName}', please make a valid choice "}


        # return {"platform":"Invalid Choice"}
        # if "youtube" in Platform:
        #     list_resp = fetchYoutubePlayList(url_provided)
        #     return {"Platform": "youtube","RawData": list_resp}

        if "resso" in Platform:
            list_resp = fetchRessoPlayList(url_provided)

            # the below line is to make a imported list to youtube 
            returnedVideoList = searchAndAddToListOnYoutube(list_resp)
            print(returnedVideoList)

            createPlaylistOnYouTube(list_resp["playlistname"],returnedVideoList)
            return {"Platform":  "resso","RawData": list_resp}

        elif "spotify" in Platform:
            list_resp = fetchPlaylistDetail(url_provided)

            # the below line is to make a imported list to youtube 

            returnedVideoList = searchAndAddToListOnYoutube(list_resp)

            # print(f"the returnedVideoList\n===============\n{returnedVideoList}\n==================\n///////////////////////////")
            # the below line is to add to playlist of youtube
            createPlaylistOnYouTube(list_resp["playlistname"],returnedVideoList)

            return {"Platform": "spotify","RawData": list_resp}
        # end
        return {"Note":f"Platform choosen is '{actualName}', please make a valid choice "}

class people(Resource):
    def get(self,name):
        for x in Data:
            if x["Data"] == name:
                return x
        return {"Data":None}

    # def put(self):
    #     pass

    def post(self,name):
        temp = {"Data":name}
        Data.append(temp)
        return temp
    
    def delete(self,name):
        for indx ,x in enumerate(Data):
            if x["Data"] == name:
                temp=Data.pop(indx)
                return {"Note":"deleted"}


api.add_resource(HelloWorld , "/")

if __name__=="__main__":
    app.run(debug=True)