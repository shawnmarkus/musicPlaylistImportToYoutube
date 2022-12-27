""" this is the file that provides the function of generating the playlist named on the basis of the input string provided and returns the ID of the playlist """


def createPlaylist(playListname,youtube):
    # print(f"\n===============\n{youtube}\n====================\n")
    request = youtube.playlists().insert(
        part="snippet,status",
        body={
          "snippet": {
            "title": playListname,
            "description": f"added {playListname} ",
            "defaultLanguage": "en"
          },
          "status": {
            "privacyStatus": "public"
          }
        }
    )

    try:
      response = request.execute()
      print(response["id"])
      return response["id"]
    except Exception as err:
      print(err)
      return err
      