let docsbutton=document.getElementById(
    "guidefrespo"
);

docsbutton.addEventListener(
    "click",
    function(){
        window.location.href='/guide'    //only when we need to view pages and shit like that 
    }
)

let convertplaylist=document.getElementById(
    "convert_btn" //this is the id for that division in html
);

convertplaylist.addEventListener(
    "click",
    function(){
        console.log("button clicked");
        let playlist_url=document.getElementById(
                                "playlist_url"
        ).value;
        console.log(playlist_url);
        fetch(
            "/convertplaylists",
            {
                method:"POST",   //here we are sending data to server so POST

                headers:{
                    "Content-Type":"application/json"  //the content is of the form of json file 
                },
                body:JSON.stringify({
                    playlist_url:playlist_url  //content gets converted into a string before sending to fastapi server
                })
            }
        )
        .then(response=> response.json())
        .then(data => {
    console.log(data);
  
    window.location.href="/processing";

});
    }
    
)
