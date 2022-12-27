import requests
from bs4 import BeautifulSoup as bs
# import pickle


# playList_link="https://m.resso.com/ZSeXQ3b6e/"

def fetchRessoPlayList(playList_link):

    req_list=requests.get(playList_link)

    # converting response into the text form
    page = req_list.text

    # creating soup 
    soup = bs(page, "html.parser")
    soup_page = soup.prettify()

    with open("webPageResso", "w") as page:
        page.write(soup_page)
        

    res = soup.find_all("li",{"class":"song-item"})
    # for repI in res:
    #     print(repI,"\n")

    playlistname = soup.find("div",{"class":"playlist-info"}).h1.text
    # print(playlistname)               

    Data = []

    for i in res:
    
        # achorTagList = i.find_all('a')
        titleAnchor = i.select('a[title]')[0]
        title = titleAnchor.attrs["title"]
        # print(i,"\n")
        # print(title,"\n")

        singer = i.find("p").text
        # print(singer,"\n")

        Data.append({
            "Title":title,
            "Singer":singer
        })

    # for e in Data:
    #   print(e,"\n")
    
    return {"Data":Data,"playlistname":playlistname}

        # print(f"Title = {title} \nSinger = {singer} ",end="\n\n")

# fetchRessoPlayList("https://m.resso.com/Zs8d8sb5o/")
