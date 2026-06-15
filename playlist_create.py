from googleapiclient.discovery import build


def playlistidfn(creds,playlist_name):

    ytobj=build('youtube','v3',credentials=creds)
    #snippet-title and descripion
    #status-privacystatus
    response=ytobj.playlists().insert(
        
        part="snippet,status" ,
                                                    
        body={
            "snippet":{
                "title":playlist_name,
                "description": f"converted from  spotify:{playlist_name}"
            },
            "status":{
                "privacyStatus":"private"
            }
        }                                           

    ).execute()
    playlistid=response['id']

    return playlistid   #return the id of the playlist created
    
# print(response)#the response we get back from youtube