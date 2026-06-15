import spotipy   #helps to talk to spotifyAPI
from spotipy.oauth2 import SpotifyOAuth    #handles login and shit
import psycopg2


#the database is being created in this step 


sp=spotipy.Spotify(auth_manager=SpotifyOAuth(
client_id="e0c56dcf3b484da7990cdad4dff6921a",
    client_secret="492b4fb1f32e496ab33a710a98692a09",
    redirect_uri="http://127.0.0.1:8888/callback",
    scope="playlist-read-private playlist-read-collaborative"
))


#result=sp.current_user_playlists()

# for playlist in result['items']:
#     print( playlist['name'])   #spotify access playlist internally using playlist id 
#     print(playlist['id'])
#     print("\n")       



def playlistsp(playlistid):
    playlistname=sp.playlist(playlist_id=playlistid)
    
    conn=psycopg2.connect(database="Frespo",
                    user="postgres",
                    password="88482",
                    host="localhost",
                    port=5432)
    curr=conn.cursor()
    tracks=sp.playlist_tracks(playlist_id=playlistid)



    # print(tracks['total'])
    # print(tracks['limit'])
    #all_songs=[]
  
    curr.execute(
    """
    SELECT id FROM playlists
    WHERE sp_playlist_id = %s
    """,
    (playlistid,)
    )

    existing_playlist = curr.fetchone()

    if existing_playlist:
        playlistid_db = existing_playlist[0]

    else:

        curr.execute(
            """INSERT INTO playlists(sp_playlist_id, playlist_name)
            VALUES(%s, %s) RETURNING id""", 
            (playlistid, playlistname['name'])
    )

    
        playlistid_db=curr.fetchone()[0]    #this will give the id of the playlist stored right now in db
    while True:
        
        #all_songs.extend(tracks['items'])
        for song in tracks['items']:

            if song['item'] is None:
                continue
            song_name=song['item']['name']
            artist_name=song['item']['artists'][0]['name']
            #query=song_name + " " + artist_name

            curr.execute(
                """
                SELECT 1
                FROM songs
                WHERE playlist_id= %s  
                AND song_name = %s
                AND artist_name= %s
                """,
                (playlistid_db,song_name,artist_name)
            )

            if curr.fetchone():
                continue


            curr.execute("""insert into songs(playlist_id,song_name,artist_name)
                         values(%s,%s,%s)""",(playlistid_db,song_name,artist_name))
            
        if tracks['next']:
            tracks = sp.next(tracks)
        else:
            break
    conn.commit()
    curr.close()
    conn.close()
    return playlistname['name'],playlistid_db
    # for q in youtube_queries:
    #     print(q)
    # print(len(all_songs))

