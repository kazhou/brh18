# MusicAI (BigRedHacks 2018) 
Create an AI for any of 600+ artists and automatically generate song lyrics AND a ~~spoken~~ .wav file for them! 
Hackathon project for BigRedHacks 2018. Resources and tools used: [Song Lyrics (Kaggle)](https://www.kaggle.com/mousehead/songlyrics), [Markovify](https://github.com/jsvine/markovify), [Watson Text-To-Speech API](https://console.bluemix.net/catalog/services/text-to-speech)

## Examples:

Taylor Swift:

Fall Out Boy:


## How to use:
Download the project and open a command line/terminal. To create the AI for an artist, type:
```bash
$ python song_scrape.py "{Artist Name}"
```
This will compile a .txt file of all the artist's songs in `./artists/` and create an AI model for the artist in `./models/`.
To generate new song lyrics and .wav file, decide whether the voice should be `"f"` for female or `"m"` for male. Then (if `"f"` for example), run:
```bash
$ python song_gen.py "{Artist Name}" "{New Song Name}" "f"
```
This will generate the new song in .txt file in `./new_songs/` and create a .wav for the song in `./song_files/`.



