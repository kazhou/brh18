import sys
import pandas
import string
import re
import csv

df = pandas.read_csv("taylor_swift_lyrics.csv", encoding = 'unicode_escape')
print(df)

print(df['track_title'].nunique()) #94 songs

#track name | lyrics

titles = df['track_title'].unique()
for song_index in range(len(titles)):
    song = titles[song_index]
    song = re.sub(r'[^\w\s]','',song) #remove

    f_name = './tswift_songs/' + song +'.txt'
    print(f_name)
    # rows of lyrics of song 'song_index'
    lyric_rows = df[df['track_title'] == titles[song_index]]['lyric']
    #write all lyrics to tswift_songs directory
    # lyric_rows = lyric_rows.to_frame()
    # for i in range(len(lyric_rows)):
    #     lyric_rows[i] = re.sub(r'[^\"]',"'",lyric_rows[i]) #replace quotes

    lyric_rows.to_csv(f_name, header=None, index=None, sep=' ',
     mode='a',encoding = 'utf_8') #quoting = csv.QUOTE_NONE


# write all songs to their own files, sentiment analyze each song
# train model on positve songs
# train model again of negative songs
# write pos and neg songs!
