"""
the below function is used to extract the meta data of the provided spotify playlist link

"""


def fetchPlaylistDetail(playlistUri2):
    
    import time
    from spotifyFuntion import createSpotifyObject,get_playlist_Id,getTrackData 

    spotifyObject = createSpotifyObject()

    playlistName = "random"
    playlistDescription = "just to check"

    # to create a playlist
    # spotifyObject.user_playlist_create(user=username, name=playlistName,public=True,description=playlistDescription)

  
    # get playlist id 
    playlistId = get_playlist_Id(playlistUri2)

    playlistNameExtract = spotifyObject.playlist(playlistId)["name"]
    # print(playlistNameExtract)

    # import json
    # with open("playlistNameExtract.txt","w") as writeRes:
    #     writeRes.write(json.dumps(playlistNameExtract))

    track_Id_list = [x["track"]["uri"].split(":")[-1] for x in spotifyObject.playlist_tracks(playlistId)["items"]]

    # print(track_Id_list)

    # print(getTrackData(track_Id_list[0]))

    Data = []

    for trackId in track_Id_list:
        time.sleep(0.2)
        print(getTrackData(spotifyObject,trackId))

        Data.append(getTrackData(spotifyObject,trackId))

    return {"Data":Data,"playlistname":playlistNameExtract}




# playlistUri2 ="https://open.spotify.com/playlist/37i9dQZF1DWXnexX7CktaI?si=c3f5385512614ebb"
# playlistUri3="https://open.spotify.com/playlist/1Baep90KNiOIupOs5F8sMa?si=aaee6dc21fa14ea7"

# fetchPlaylistDetail(playlistUri3)
