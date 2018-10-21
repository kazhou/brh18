import sys
import pandas
import string
import re
import csv
from textblob import TextBlob
import markovify
import json

#generate ai for an artist
artist = str(sys.argv[1]) #double quotes

df = pandas.read_csv("./songlyrics/songdata.csv", encoding = 'unicode_escape')
# len(df['artist'].unique()) #643
# print(df.columns) #['artist', 'song', 'link', 'text']
# print(df['artist'].unique())
#'ABBA', 'Ariana Grande', 'Celine Dion', 'Fall Out Boy', 'Twenty One Pilots',
# 'One Direction', 'High School Musical', 'Lady Gaga', 'Justin Bieber',
#'Justin Timberlake', 'Kanye West', 'Kari Jobe',
#       'Kate Bush', 'Katy Perry'

f_name = './artists/'+artist+'.txt'
try: #artist
    artist_df = df[df['artist'] == artist]
    print("Artist found")
    lyrics = artist_df['text']
    all_lyr = lyrics.str.cat(sep="\n")
    all_lyr.strip(string.punctuation)
    fn = open(f_name,'w')
    fn.write(all_lyr)
    fn.close()
    print("Lyrics compiled")
except:
    print('Artist not found')

# Get raw text as string.
with open(f_name) as f:
    text = f.read()

# print(text)
# Build the model.
text_model = markovify.NewlineText(text)
model_json = text_model.to_json()
# print(model_json)
m_file = './models/'+artist+'.json'
with open(m_file, 'w') as outfile:
    json.dump(model_json, outfile)

print("Model created")
