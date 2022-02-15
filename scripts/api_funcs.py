from email import header
from wsgiref import headers
import requests
import base64, json

authUrl = "https://accounts.spotify.com/api/token"

authHeader = {}

authData = {}

# Base64 Encode Client ID and Client Secret



def getAccesToken(client_id, client_secret):

	message = f"{client_id}:{client_secret}"
	message_bytes = message.encode('ascii')
	base64_bytes = base64.b64encode(message_bytes)
	base64_message = base64_bytes.decode('ascii')

	authHeader['Authorization'] = "Basic " + base64_message
	authData['grant_type'] = "client_credentials"

	res = requests.post(authUrl, headers=authHeader, data=authData)
	responseObject = res.json()

	accesToken = responseObject['access_token']
	return accesToken



def GetPlaylistTracks(accesToken, playlistID):
	playlistEndPoint = f"https://api.spotify.com/v1/playlists/{playlistID}"

	getHeader = {
		'Authorization' : "Bearer " + accesToken
	}

	res = requests.get(playlistEndPoint, headers=getHeader)

	playlistObj = res.json()

	return playlistObj




def GetAlbum(accesToken, albumID):
	albumEndPoint = f"https://api.spotify.com/v1/albums/{albumID}"

	getHeader = {
		'Authorization' : "Bearer " + accesToken
	}

	res = requests.get(albumEndPoint, headers=getHeader)
	print(res)
	albumObj = res.json()

	return albumObj

def GetTrack(accesToken, trackID):
	trackEndPoint = f"https://api.spotify.com/v1/tracks/{trackID}"

	getHeader = {
		'Authorization' : "Bearer " + accesToken
	}

	res = requests.get(trackEndPoint, headers=getHeader)

	trackObj = res.json()

	return trackObj


def GetAudioFeatures(accesToken, trackID):
	audiofeaturesEndPoint = f"https://api.spotify.com/v1/audio-features/{trackID}"

	getHeader = {
		'Authorization' : "Bearer " + accesToken
	}

	res = requests.get(audiofeaturesEndPoint, headers=getHeader)

	audiofeaturesObj = res.json()

	return audiofeaturesObj

def get_audiofeatures(featurelist):
	data = []
	for item in featurelist:
		data.append(featurelist[item])
	return data[:11]

def get_playlist_data(tracklist):
	all_data = []
	for item in tracklist['tracks']['items']:
		data = {
			'Artist' : item['track']['album']['artists'][0]['name'],
			'Name' : item['track']['name'],
			'Release_Date' : item['track']['album']['release_date'],
			'Type' : item['track']['type'],
			'Popularity' : item['track']['popularity'],
			'Id' : item['track']['id']
		}
		all_data.append(data)
	return all_data



def get_album_data(albumlist, accesToken):
	name_list = ['Danceability', 'Energy', 'Key', 'Loudness', 'Mode', 'Speechiness', 'Acousticness', 'Instrumentalness', 'Liveness', 'Valence', 'Tempo']
	alb_data = []

	for item in albumlist['tracks']['items']:
		track = {
			'Album_Popularity' : albumlist['popularity'],
			'Album_Name' : albumlist['name'],
			'Album_Owner' : albumlist['artists'][0]['name'],
			'Release_Date' : albumlist['release_date'],
			'Song_Name' : item['name'],
			'Track_Nr' : item['track_number'],
			'Duration_Mins' : round(item['duration_ms'] / 60000, 2),
			'Track_Id' : item['id']
		}

		track_list = GetTrack(accesToken, track['Track_Id'])
		track["Track_Popularity"] = track_list["popularity"]

		featurelist = GetAudioFeatures(accesToken, track['Track_Id'])
		my_list = get_audiofeatures(featurelist)
		for i in range(len(name_list)):
			track[name_list[i]] = my_list[i]

		all_artists = []
		for artist in item['artists']:
			all_artists.append(artist['name'])
		track['Artists'] = all_artists
		 
		alb_data.append(track)
	return alb_data