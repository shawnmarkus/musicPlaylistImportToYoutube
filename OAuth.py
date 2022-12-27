from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import json


import os
import urllib.parse as Parse
import pickle


from  addItemsToPlaylist import addItemsToPlaylist
from  createPlaylist import createPlaylist


def youTubeOAuth():

    # important vars
    SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl","https://www.googleapis.com/auth/youtube",]
    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_credentials.json"
    creds = None    


    # print("--------------------------------------------------------------------\n")                            
    if os.path.exists("token.pickle") and os.path.getsize("token.pickle") != 0:
        print("Loading the credentials from existing file...")
            
        with open("token.pickle", "rb") as token:
                    creds = pickle.load(token)

    #     if there are no (valid) credentials availablle, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
                print("getting the fresh token...")
                creds.refresh(Request())
        else:
            print("fetching new token..")
            #Flow.from_client_secrets_file("FILE_PATH",SCOPES,REDIRECT_URI="") 
            flow = InstalledAppFlow.from_client_secrets_file(client_secrets_file, SCOPES)
            # prompt -- to get the refresh token every time
            creds = flow.run_local_server(port=5500,prompt="consent",authorization_prompt_message="")
            
    with open("token.pickle", "wb") as token:
        #save the credentials for the next run
        print("Saving the credentials into the file for future references..")
        pickle.dump(creds, token)

    # returning the build because The (open-sourced) Python API Client Library includes discovery.build which generates the resources for the service that you provide it. actually the google has facilitate this service for auto code generation for the service which is requested .
    try:
        youtube = build(api_service_name, api_version,credentials=creds)
        return youtube
    except Exception as err:
        print(f"error that occured is : {err}")
        return "Failed"

     

# building the call request body
youtube = youTubeOAuth() #its is necessary part 



# ======================================================================================================

#///////////////////was main///////////createdPlaylistId = createPlaylist("fav music",youtube)

# print(f'\n\n\n==================================+++++++++====\n\n\n\n createPlaylistID = {createdPlaylistId}\n\n\n\n\n===========++++++++++++++===================')

# =======actual code==========
# adding playlist and capturing the return value into response ----------------
# request = youtube.playlists().insert(
#         part="snippet,status",
#         body={
#           "snippet": {
#             "title": "Sample playlist created via API",
#             "description": "This is a sample playlist description.",
#             "defaultLanguage": "en"
#           },
#           "status": {
#             "privacyStatus": "public"
#           }
#         }
#     )
# response = request.execute()
# print(response)


# ======================================================================================================

# try and test --working fine 

# request = youtube.playlistItems().list(part="status",playlistId="PL1PA9IVu7cZ9PPSinboVE23HVaKLlaO4l")
# response = request.execute()
# print(response)

# =====================================================================================================

# adding playlistIems and capturing the return value into PlaylistItemsResponse ----------------

# videoIds = ["VK9PGcGx2xk","v2IGNN7CA4M","2JBYnvUlAEc"]

# ///////////////////was main///////////addItemsToPlaylist(videoIds,createdPlaylistId,youtube)

# ========actual code============
# for videoId in videoIds:
 
#     request_body = youtube.playlistItems().insert(
#       part = "snippet,id,status,contentDetails",
#       body = {
#         "snippet":{
#            "playlistId": "PLWyoI84HSUvH8PxUHpRU4SplOgeZdHhDT", #an actual playlistid PLWyoI84HSUvH8PxUHpRU4SplOgeZdHhDT
#             "position": 0,
#             "resourceId": {
#               "kind": "youtube#video",
#               "videoId": videoId
#         }
#       }
#       }
#     )

#     response = request_body.execute()
#     vd_title = response["snippet"]["title"]
#     print(f"Video {vd_title} inserted to the specified playlis\n")



