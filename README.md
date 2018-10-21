# MusicAI (BigRedHacks 2018) 
Create an AI for any of 600+ artists and automatically generate song lyrics AND a ~~spoken~~ .mp3 file for them! 
Hackathon project for BigRedHacks 2018. Resources and tools used: [Song Lyrics (Kaggle)](https://www.kaggle.com/mousehead/songlyrics),  [pandas](https://pandas.pydata.org/pandas-docs/version/0.18/index.html), [Markovify](https://github.com/jsvine/markovify), [Watson Text-To-Speech API](https://console.bluemix.net/catalog/services/text-to-speech)

## Examples:

<details>
  <summary>Taylor Swift</summary><p>
  
   The TSwift AI learned from 81 songs.
 
    Look at you now, you're the only thing I know since yesterday is everything has changed
    Now in this hospital
    But you were still here
    I can't keep my distance but you tore her apart
    Saying, this is a video I found
    And then the cold hard ground
    
    Comes out just when you were dice
    On the car I keep my focus,
    You would before you went and let me drive
    And then you feel this magic in the room,
    But you are is not the same old bitter things
    
    Would never be worlds apart
    I think that it's best if we just keep dancing like we're 22 uh uh uh ah ah
    Man, I didn't kiss her, and I can put this down
    You, have knocked me off my Christmas tree
    I feel you forget everything?
    
    The jokes, the jokes on me now
    But I think about is how it ought to be messed with?
    Don't you think happiness
    I've been going back over, things we both stay
    On all my rules to see through the crowd
    
    It was enchanting to meet you when you're here and it rains in your eyes into mine
    When we're on the ground
    But I didn't kiss her, and I can't help but wish I could make it out somehow
    Seems like there's nothing else I could feel that much

  
 </p></details>

<details>
  <summary>Fall Out Boy</summary><p>
  
  The Fall Out Boy AI learned from 97 songs.
  
    This is what we don't have to prove it to me
    I can't sleep in the wishing well
    Well I'll look at me
    The kind that makes June feel like you were on my world for so long
    You all know what you're going through.
    I'll walk myself away from making it

    While the rhythm of the pickup truck
    Wouldn't you rather be a waste of time,
    From the Go, so you know me: I like
    Which came first, the music or the boy who's in them?
    Cry on the couch so all the girls whose lips couldn't move fast enough

    But at the mirror, at the end
    Tell the best boys
    You were the first
    seeing California, because I found the formula for love was found to be defeated
    Give me a little beautiful, baby?

    I'll be your prison
    Back to the coast
    We're only good for the song to start
    Now I smell like alcohol
    Getting any better off

    Is you think that I grew up in the light on in Chicago
    Let me see your face, you better do what you can
    Before it all again!
    A joke of a lunatic?

  
</p></details>

<details>
  <summary>One Direction</summary><p>
  
  The 1D AI learned from 98 songs.
    
    Tight dress with the freckles on your own
    What a feeling to be like them
    You want to be right here in it's cage
    I can feel the same thing
    She's the one that's in command
    Waiting for my fantasy to crash and burn in it all yeah, who could've planned it?

    Nothing you can take it
    I'm half a blue sky
    I'll take you there, take you there, yeah I know they'll be coming to find you but I figured out from the playground
    Cause I wanna do
    So tell me what you do is say that I won't hesitate no more, no more

    And giving back is all you do
    Driving to your feet
    Baby let me go, don't let me kiss you once now I can't hold you down,
    Everybody wanna take it to be a good night
    Baby you light up every second of the things I want

    It's so right you know you wanna cry or fall apart
    Open up your almost done
    Same old shh but we never say never,
    But I'm not scared of love hate
    All I ever wanted was the best but expecting the worst,

    Don't make me strong?
    Hey, I don't wanna take you and say it all
    Need to take it slow
    We built it up Go
    We did that when I saw your face

    Remember the day that we been through
    To get me out
    At the end of the verses, well, they've got me lifted off my feet
    Baby let me kiss you once now I can't give up
 </p></details>

## How to use:
Download the project and open a command line/terminal. To create the AI for an artist, type:
```bash
$ python song_scrape.py "{Artist Name}"
```
This will compile a .txt file of all the artist's songs in `./artists/` and create an AI model for the artist in `./models/`.
To generate new song lyrics and .mp3 file, decide whether the voice should be `"f"` for female or `"m"` for male. Then (if `"f"` for example), run:
```bash
$ python song_gen.py "{Artist Name}" "{New Song Name}" "f"
```
This will generate the new song in .txt file in `./new_songs/` and create a .mp3 for the song in `./song_files/`.

## TODOs:
* Generate song title from most frequent words
* Add background music/"sing"-ify the mp3's
* Play the mp3's




