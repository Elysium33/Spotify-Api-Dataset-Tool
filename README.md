# Spotify-Api-Data-Generator


This is an app I've built to generate datasets that contain data about tracks/albums/playlists that are available on Spotify.
To do this I used the Spotify API and Pandas library.

The functions in the "spotify_funcs" script are used to extract data about tracks, albums or playlists.

The "spotify_api" script reads a csv file that contains different album links afterwhich it concatenates each pandas dataframe created and finally it writes the dataframe to csv and a SQL database.


The scripts folder contains the module and main file that are used for the task above.
I used this app to generate a dataset that contains the track popularity, album popularity, tempo, liveness etc. for 120 hip-hop albums from 2010 to 2021.
There is also an SQL file that queries the data for some analysis.

