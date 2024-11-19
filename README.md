# Coordinate-Based Playlist Generator

This web application allows users to generate Spotify playlists based on geographic coordinates (latitude and longitude). By entering the coordinates, the app uses **OpenCageAPI** to retrieve location data and **SpotifyAPI** to create a playlist tailored to the location. Perfect for experiencing music related to different parts of the world!

![interface](gh-assets/CookieLocation.png)

## Features

- Enter **latitude** and **longitude** to get a playlist based on the location.
- Uses **OpenCageAPI** to convert coordinates into location names.
- Uses **SpotifyAPI** to generate music playlists related to the given location.
- Simple and easy-to-use interface for generating location-based playlists.



## Tech Stack

- **Frontend**: HTML, CSS
- **Backend**: Python (Flask/Django)
- **APIs**: OpenCageAPI, SpotifyAPI
- **Database**: None (using API data)



## Prerequisites

To run the application locally, you will need:
- A **Spotify API** account and **API key** for generating playlists.
- A **OpenCageAPI** account and **API key** for geocoding coordinates into location names.



## Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/coordinate-playlist-generator.git
```

### 2. Install dependencies

Make sure you have Python installed. Then, use `pip` to install the necessary Python packages.

```bash
pip install -r requirements.txt
```

### 3. Set up your API keys

- **Spotify API**: Create an application on the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications) and get your API keys.
- **OpenCageAPI**: Sign up on [OpenCageData](https://opencagedata.com/) to get your API key.

In your application, create  `.txt `or `.json`file and add your keys:

```env
spotify_keys.json (for storing your Spotify credentials):
{
  "client_id": "your_spotify_client_id",
  "client_secret": "your_spotify_client_secret",
  "redirect": "your_spotify_redirect_uri",
  "username": "your_spotify_username"
}
```

```
with open ("OpenCage_key.txt",'r') as key_file:
	OpenCage_key = key_file.read()
	api_key = OpenCage_key
```

### 4. Run the application

After setting up your environment and configuring your API keys, you can run the application using **Command Prompt**. Follow these steps:

Open **Command Prompt** (Windows) or **Terminal** (Mac/Linux).

1. **Navigate to your project directory**:
   
   ```bash
   cd path\to\your\project
   ```
   
2. **Activate the virtual environment** (for Windows):
   ```bash
   venv\Scripts\activate
   ```

3. **Install the necessary dependencies** (`spotipy` and `flask`):
   ```bash
   pip install spotipy flask
   ```

4. **Run the Flask application**:
   ```bash
   flask run
   ```

This will set up your virtual environment, install the necessary libraries, and start the Flask server locally. 



## Usage

1. Open the app in your browser.
2. Enter the **latitude** and **longitude** coordinates in the input fields.
3. Press **"Generate Playlist"**.
4. A playlist will be generated based on the location corresponding to the coordinates you entered.



## Contributions

Feel free to fork the repository, make improvements, or open issues for any bugs or feature requests. Contributions are always welcome!

