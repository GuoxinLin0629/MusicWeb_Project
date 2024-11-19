from flask import Flask, render_template, request, redirect, url_for
import openai
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth
import webbrowser
import json
import urllib.request

with open('spotify_keys.json', 'r') as spotify_file:
    # load reads a JSON string from a file
    tokens = json.load(spotify_file)

my_client_id = tokens['client_id']
my_client_secret = tokens['client_secret']
redirectURI = tokens['redirect']
username = tokens['username']

    
scope = "user-read-private user-read-playback-state user-modify-playback-state playlist-modify-public"
token = util.prompt_for_user_token(username, scope, client_id=my_client_id, client_secret=my_client_secret, redirect_uri=redirectURI)
sp = spotipy.Spotify(auth=token)

user_id = sp.current_user()['id']
print(f"Successfully authenticated as {user_id}")

with open ("OpenCage_key.txt",'r') as key_file:
	OpenCage_key = key_file.read()

api_key = OpenCage_key


def get_playlist(latitude, longitude):
	url = f'https://api.opencagedata.com/geocode/v1/json?q={latitude}+{longitude}&key={api_key}'
	
	request = urllib.request.Request(url)
	# capture all the JSON coming back from the interwebs
	response = urllib.request.urlopen(request)
	location_json = json.loads(response.read())
	location_name = location_json['results'][0]['formatted']

	location_results = sp.search(q=location_name, type='track', limit=10)
	song_data = location_results['tracks']['items']

	song_uris = []
	
	
	for song in song_data:
		song_uris.append(song['uri'])
		my_playlist = sp.user_playlist_create(user=username, name=location_name, public=True, description="songs for {location_name}")
		sp.user_playlist_add_tracks(username, my_playlist['id'],song_uris)

	return my_playlist['id']


