import random
import urllib.parse as urllibparse 
import spotipy
from spotipy.oauth2 import SpotifyOAuth


# credentials
def createSpotifyObject():
    Client_Id = "7a64dbe9c77f451fafaccb4e52e245b6"
    Client_Secret = "fff5e33ea56b436497cf156ae39ba424"
    redirect_uri = 'http://localhost:5500/'
    scope = "playlist-modify-private playlist-modify-public"
    response_type = 'code'

    # creating some random number           
    randomNum =str(random.getrandbits(128))
    hash = int(randomNum,36)
    state =  hex(hash)



    spotifyToken = SpotifyOAuth(Client_Id,
                       Client_Secret,
                       redirect_uri,state,scope)

    auth_url = spotifyToken.get_authorize_url()

    # spotifyObject = spotipy.Spotify(auth_manager=spotifyToken)

    return spotipy.Spotify(auth_manager=spotifyToken)



def get_playlist_Id(playlist_link):
    return playlist_link.split("/")[-1].split("?")[0]


def getTrackData(spotifyObject,trackId):
    meta = spotifyObject.track(trackId)
    trackDetails = {"Title":meta["name"],"Singer":meta["artists"][0]["name"]}
    return trackDetails
