from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
# from oauth2client.tools import argparser


DEVELOPER_KEY = "AIzaSyCvq5k8yE26NlsZaA23MDMSUleJs97Flds"
YOUTUBE_API_SERVICE_NAME="youtube"
YOUTUBE_API_VERSION="v3"
youtube = build(YOUTUBE_API_SERVICE_NAME,YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)

search_response = youtube.search().list(
    q = "뽀로로", # 검색어
    order = "relevance",  #정렬방법
    part = "snippet", # 필수 매개변수
    maxResults = 10
    ).execute()



# for i in search_response['items']:

# print(search_response['items'][0]['id']['videoId'])
# print(search_response['items'][0]['id']['videoID'])
# print("###############################3")
# print(search_response['items'][0]['id']['kind'])
# print("###########################3")
# print(search_response['items'][0]['snippet']['thumbnails']['default']['url'])


# 살인마협회장
# channel_id = search_response['items'][0]['id']['channelid']

# playlists = youtube.playlist().list(
#     channeld = channel_id,
#     part = "snippet",
#     maxResults = 20
# ).execute()

# import pandas as pd

# ids=[]
# titles=[]

# for i in playlists['items'] :
#     ids.append(i['id'])
#     titles.append(i['snippet']['title'])

# df = pd.DataFrame([ids,titles]).T
# df.columns=['PlayLists','Titles']