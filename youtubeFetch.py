from pytube import YouTube , Playlist
import json


# playList_link="https://youtube.com/playlist?list=PLSyUnzaPyYgnG_pHTUKPLuT6qpNZAJ7sN"
def fetchYoutubePlayList(playList_link):

    res = Playlist(playList_link)

    if "playlist?list" in playList_link :
        print("it is a playlist")

    else:
        print("its not a playlist")  

    listOfMusic = [{i} for  i in res.url_generator()]
    
    Data = []

    for playableLink in listOfMusic:
        
        title = ""
        # print("Titile : ",end="")
        for x in str(YouTube(f"{playableLink}").title):
            if ord(x) in range(0,2500):
                # print(x,end="")
                title+=x

        # print("\n")
        Author = YouTube(f"{playableLink}").author
        # print(f"\nAuthor : {Author}")

        Data.append({
            "Title":title,
            "Singer":Author
        })

    return Data

#     for e in Data:
#         print(e,"\n")
        

# fetchYoutubePlayList("https://youtube.com/playlist?list=PLSyUnzaPyYgnG_pHTUKPLuT6qpNZAJ7sN")