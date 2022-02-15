import pandas as pd
from credentials import clientID, clientSecret, path_csv, db_user, db_pass, db_name, path_links
import time
import sqlalchemy
import api_funcs as af


if __name__ == "__main__":


	engine = sqlalchemy.create_engine(f'postgresql+psycopg2://{db_user}:{db_pass}@localhost:5432/{db_name}')
	#API requests
	token = af.getAccesToken(clientID, clientSecret)


	df = pd.DataFrame(columns=['Album_Popularity', 'Album_Name', 'Album_Owner', 'Release_Date', 'Song_Name', 'Track_Nr', 'Duration_Mins', \
		'Track_Id', 'Track_Popularity' , 'Danceability', 'Energy', 'Key', 'Loudness', 'Mode', 'Speechiness', 'Acousticness', 'Instrumentalness', \
		'Liveness', 'Valence','Tempo', 'Artists'])


	df_links = pd.read_csv(path_links + '/SpotifyLinks.csv')

	for albumID in df_links['album_links']:
		albumID = albumID.split('/')[-1]
		try:
			albumlist = af.GetAlbum(token, albumID)
			df = pd.concat([df, pd.DataFrame(af.get_album_data(albumlist, token))], ignore_index=True)
		except:
			print("Error!")
			time.sleep(31)

			
	df.to_csv(path_csv + '/Top10albums2010-2021.csv', index = False)

	df.to_sql(
			name = 'Top10albums2010-2021',
			con = engine,
			index = False,
			if_exists = 'fail'
	)
	print('Your Album Information has been added to csv and the DB.')

