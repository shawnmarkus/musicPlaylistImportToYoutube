
"""
this below function takes the list of object which is containing the name of song and may be along with the name of singer and on that basis it made query and draw the first id of the listed video
"""
from pytube import Search

def searchAndAddToListOnYoutube(dataList):
    videoIdList = []
    # print("\n=====\n",dataList)
    for i in dataList["Data"]:
        # print(f" the item searched is {i}\n\n")
        if i["Singer"]:
            response = Search(f'{i["Title"]} by {i["Singer"]}')
        else:
            response = Search(f'{i["Title"]}')
        print(f"the id for {i['Title']} is id = {response.results[0].video_id}\n")
        videoIdList.append(response.results[0].video_id)
    # pass
    return videoIdList

# searchAndAddToList(data)