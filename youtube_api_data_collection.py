import secret
import pandas as pd

from googleapiclient.discovery import build

channel_id = 'UCi42yeT0_OLeouUQhDBVZjQ'
playlist_id = 'UUi42yeT0_OLeouUQhDBVZjQ'


youtube = build('youtube', 'v3', developerKey={secret.api_key})

# get youtube channel information

def get_channel_stats(youtube, channel_id):
    
    channel_info_data = []
    
    request = youtube.channels().list(
        part='snippet,contentDetails,statistics', 
        id=channel_id
    )
    response = request.execute()
    
    for item in response['items']:
        data = {'channel': item['snippet']['title'],
                'subscribers': item['statistics']['subscriberCount'],
                'views': item['statistics']['viewCount'],
                'video_count': item['statistics']['videoCount'],
                'playlist_id':item['contentDetails']['relatedPlaylists']['uploads']
                }
        
        channel_info_data.append(data)
        df_channel_info = pd.DataFrame(channel_info_data)
    
    return df_channel_info

# get video ids, store it and use it to extract youtube videos information

def get_video_ids(youtube, playlist_id):

    video_ids = []

    request = youtube.playlistItems().list(
        part="snippet, contentDetails",
        playlistId=playlist_id,
        maxResults=50
    )
    response = request.execute()

    for item in response['items']:
        video_ids.append(item['contentDetails']['videoId'])

    next_page_token = response.get('nextPageToken')
    while next_page_token is not None:
        request = youtube.playlistItems().list(
            part="snippet, contentDetails",
            playlistId=playlist_id,
            maxResults=50,
            pageToken=next_page_token
        )
        response = request.execute()

        for item in response['items']:
            video_ids.append(item['contentDetails']['videoId'])

        next_page_token = response.get('nextPageToken')

    return video_ids

# get youtube videos information

def get_video_details(youtube, video_ids):
    all_video_info = []

    for i in range(0, len(video_ids), 50):
        request = youtube.videos().list(
            part="snippet,contentDetails,statistics",
            id=','.join(video_ids[i:i+50])
        )
        response = request.execute()
        
        
        for video in response['items']:
            stats_to_keep = {
                'snippet': ['title', 'publishedAt'],
                'statistics': ['viewCount', 'likeCount', 'commentCount'],
                'contentDetails': ['duration']
            }
            
            video_info = {}
            video_info['video_id'] = video['id']

            for key in stats_to_keep.keys():
                for value in stats_to_keep[key]:
                    video_info[value] = video[key][value]

            all_video_info.append(video_info)
            df_video_info = pd.DataFrame(all_video_info)
            
    return df_video_info

# main function

def main():
    df_channel_info = get_channel_stats(youtube, channel_id)
    df_channel_info.to_csv('channel_info.csv', index=False)
    
    video_ids = get_video_ids(youtube, playlist_id)
    
    df_video_info = get_video_details(youtube, video_ids)
    df_video_info.to_csv('video_info.csv', index=False)

if __name__ == '__main__':
    main()
