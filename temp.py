# For Fetching Comments 
from googleapiclient.discovery import build 
# For filtering comments 
import re 
# For filtering comments with just emojis 
import emoji
# Analyze the sentiments of the comment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
# For visualization 
import matplotlib.pyplot as plt

API_KEY = 'AIzaSyA0ihrq03WQegEaVdQmC412hwTl5EipN5U'

# initializing youtube data api
youtube = build('youtube', 'v3', developerKey=API_KEY)

# taking input from the user for video id and playlist id.
video_id = input('Enter Youtube Video URL: ')[-11:]
print("Video id: " + video_id)

# Getting the ChannelID of the user who uploaded the video
video_response = youtube.videos().list(
    part='snippet',
    id = video_id
).execute()

# Splitting the response for ChannelID
video_snippet = video_response['items'][0]['snippet']
channel_id = video_snippet['channelId']
print("Channel ID: "+channel_id)

# EXAMPLE VIDEO URL https://www.youtube.com/watch?v=avz06PDqDbM


#Fetching comments 
print("Fetching commments...")
comments = []
nextPageToken = None 

while len(comments)<600:
    request = youtube.commentThreads().list(
        part = 'snippet',
        videoId = video_id,
        maxResults = 100, # fetching 100 comments per request
        pageToken = nextPageToken
    )
    response = request.execute()
    for item in response['items']:
        comment = item['snippet']['topLevelComment']['snippet']
        # Checking if comment is not from the video uploader
        if comment['authorChannelId']['value'] != channel_id:
            comments.append(comment['textDisplay']) 
    nextPageToken = response.get('nextPageToken')

    if not nextPageToken:
        break

comments[:5]