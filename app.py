#fastapi file
from fastapi import FastAPI,Request
from fastapi.staticfiles import StaticFiles
from main import playlistsp
from fastapi.templating import Jinja2Templates
from songs_insert import youtube_convert
from spotipy.exceptions import SpotifyException
from fastapi import BackgroundTasks
import psycopg2
from db import database_connection
app=FastAPI()


conversion_status={
    "completed":False,
    "playlist_url":None,
    "error":None
}

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

templates = Jinja2Templates(
    directory="templates"
)


conn=database_connection()

curr=conn.cursor()

@app.get("/")
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

@app.get('/songs')
async def get_songs():   #async def is use cuz when we use that when the funtion spends some time waiting for something like api calls and shit 
    curr.execute("""Select * from playlist_songs""")
    db_songs=curr.fetchall()
    songs=[]
    for song in db_songs:
        
        songs.append({
            "id":song[0],
            "query":song[1],
            "title":song[2],
            "video_url":f"https://youtube.com/watch?v={song[3]}"
            
        })
    
    return songs

@app.post('/convertplaylists')

async def converttoplay(request:Request,background_task:BackgroundTasks):    #backgroundtasks enables us to make the backend work without the user knowing by making the frontend do something for the user using a file
    conversion_status["completed"]=False
    conversion_status["playlist_url"]=None
    conversion_status["error"]=None

    data=await request.json()  #here we need to use await cuz without that it will not return dict,await gives us a promise that it will return after we do the coroutine 
    result=data['playlist_url'].split('/')[-1].split('?')[0]  #playlistid from spotify

    background_task.add_task(
        process_playlist,
        result
    )
   


    return {"success": True}
    
    
def process_playlist(result):

    try:

        print("PROCESS PLAYLIST STARTED")

        playlistname,playlistdb_id = playlistsp(result)

        print("SPOTIFY DONE")

        ytplaylistid = youtube_convert(playlistname,playlistdb_id)

        conversion_status["completed"]=True
        conversion_status["playlist_url"]=ytplaylistid["playlist_url"]
        print("YOUTUBE DONE")
    except SpotifyException as e:
        if e.http_status == 403:  #cuz error 403 is the forbidden error 
            conversion_status["error"]="The playlist is private or inaccessible.Please use one of your own playlists"
        else:
            conversion_status["error"]="SPOTIFY ERROR OCCURRED"


@app.get('/guide')
def guide(request:Request):    #here we use type hint :Request is the type hint.
    return templates.TemplateResponse(
        request=request,
        name="guide.html"
    )


@app.get('/processing')
def processing(request:Request):
    print("Processing route reached")
    return templates.TemplateResponse(
        request=request,
        name="processing.html",


    )

@app.get('/status')
def status():
    return conversion_status


@app.get("/success")
def success(request:Request):
    return templates.TemplateResponse(
        request=request,
        name="success.html",
        context={
            "playlist_url":conversion_status["playlist_url"]
        }
    )

@app.get("/error")
def error(request:Request):
    return templates.TemplateResponse(
        request=request,
        name="error.html",
        context={
            "error_message":conversion_status["error"]
        })
