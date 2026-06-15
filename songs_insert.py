from googleapiclient.discovery import build
from youtube_auth import authenticate
from playlist_create import playlistidfn
from googleapiclient.errors import HttpError
import psycopg2
import time
def youtube_convert(playlistname,playlistdb_id):  #convert the songs in db to songs in youtube.
    creds=authenticate()


    playlistid=playlistidfn(creds,playlistname)   #playlistid from playlist_create.py ie what is the new playlistid to which we need to add songs

    ytobj=build('youtube','v3',credentials=creds)

    conn=psycopg2.connect(database="Frespo",
                        user="postgres",
                        password="88482",
                        host="localhost",
                        port="5432")
    curr=conn.cursor()

    curr.execute(
    """
    SELECT song_name, artist_name
    FROM songs
    WHERE playlist_id = %s
    """,(playlistdb_id,))

    inserted_songs=[]
    songs=curr.fetchall()
    for song in songs:
        query=f"{song[0]} {song[1]}"
        
        try:

            resp = ytobj.search().list(
                q=query,
                type="video",
                part="snippet",
                maxResults=1
            ).execute()

            videoId = resp['items'][0]['id']['videoId']
        
            ytobj.playlistItems().insert(

                part="snippet",

                body={
                    "snippet":{

                        "playlistId":playlistid,
                        "resourceId":{
                            "kind":"youtube#video",
                            "videoId":videoId
                        }

                    }
                }
            ).execute()

            
            inserted_songs.append(song[0])

            time.sleep(6)

        except HttpError as e:
            print(e)
            continue #if i give break then  it will go out of the entire loop,continue skips just one song
    curr.close()
    conn.close()
    playlist_url=f"https://www.youtube.com/playlist?list={playlistid}"
    return{
        "message":"Songs inserted successfully",
        "songs" : inserted_songs,
        "playlist_url":playlist_url
        
    }