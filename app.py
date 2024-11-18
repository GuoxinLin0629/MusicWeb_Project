from flask import Flask, render_template, request
from coodinate_spotify import get_playlist

# Initialize Flask application
app = Flask(__name__)

# default_coordinate = "default_latitude=51.47492, default_longitude=-0.29300"
# defaults = {"latitude": 51.47492, "longitude":0.29300}

default_lat = 48.88520
default_long = 2.34361
@app.route('/')
def index():
    my_playlist = get_playlist(default_lat, default_long)
    return render_template('index.html', lat=default_lat, lon=default_long)

@app.route('/', methods=['POST'])
def index_post():
	user_lat = request.form['req_lat']
	user_lon = request.form['req_lon']
	my_playlist = get_playlist(user_lat, user_lon)
	return render_template('index.html', playlist_id=my_playlist, lat=user_lat, lon=user_lon)

