""" this fuctions add the all the items provided in list of video ids to the playlisy specified playlistID provided by input """


def addItemsToPlaylist(itemList,playlistId,youtube):
    # print(f"\n===============\n{itemList}\n====================\n")
    import time
    for videoId in itemList:
        time.sleep(0.3)
        request_body = youtube.playlistItems().insert(
        part = "snippet,id,status,contentDetails",
        body = {
            "snippet":{
            "playlistId": playlistId, #an actual playlistid PLWyoI84HSUvH8PxUHpRU4SplOgeZdHhDT
                "position": 0,
                "resourceId": {
                "kind": "youtube#video",
                "videoId": videoId
            }
        }
        }
        )

        try:
            response = request_body.execute()
        except Exception as err:
            print(err)

        vd_title = response["snippet"]["title"]
        print(f"Video {vd_title} inserted to the specified playlis\n")
        
    return 

