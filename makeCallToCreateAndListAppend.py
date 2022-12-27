from OAuth import youTubeOAuth
from  addItemsToPlaylist import addItemsToPlaylist
from  createPlaylist import createPlaylist


def createPlaylistOnYouTube(playListName,videoIdList):
    youtube = youTubeOAuth()
    createdPlaylistId = createPlaylist(playListName,youtube)
    print("playlist created and now moving on to adding item")
    addItemsToPlaylist(videoIdList,createdPlaylistId,youtube)
    return 

