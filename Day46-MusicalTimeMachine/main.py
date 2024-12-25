# Udemy: Master Python by building 100 projects in 100 days
# Dec 24, 2024
# Day 46 - Create a Spotify Playlist using the Musical Time Machine
from functions import get_100_songs, get_Spotify, create_playlist

if __name__ == '__main__':
    # Prompt the user to input a date in the format YYYY-MM-DD
    date = input('Which year do you want to travel to? '
             'Type the date in this format YYYY-MM-DD: ')
    # Fetch the top 100 songs from the Billboard Hot 100 chart for the given date
    list_of_songs = get_100_songs(date)

    songs_uris = []
    year = date.split('-')[0]

    # Authenticate and get a Spotify client
    sp = get_Spotify()

    # Search Spotify for each song by title and year, and collect their URIs
    for title in list_of_songs:
        results = sp.search(q=f"track:{title} year:{year}", type="track")
        try:
            songs_uris.append(results['tracks']['items'][0]['uri'])
            # print(songs_uris)
        except IndexError:
            print('Track cannot be found')

    # Create a new private playlist on Spotify and add the collected songs to it
    create_playlist(sp, date, songs_uris)
