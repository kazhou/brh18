import sys
import pandas
import string
import re
import csv
from textblob import TextBlob

df = pandas.read_csv("taylor_swift_lyrics.csv", encoding = 'unicode_escape')
print(df)

print(df['track_title'].nunique()) #94 songs

#track name | lyrics

# write all songs to their own files,
titles = df['track_title'].unique()
for song_index in range(len(titles)):
    song = titles[song_index]
    song = re.sub(r'[^\w\s]','',song) #remove

    f_name = './tswift_songs/' + song +'.txt'
    print(f_name)
    # rows of lyrics of song 'song_index'
    lyric_rows = df[df['track_title'] == titles[song_index]]['lyric']
    #write all lyrics to tswift_songs directory

    # for i in range(len(lyric_rows)):
    #     lyric_rows[i] = re.sub(r'[^\"]',"'",lyric_rows[i]) #replace quotes

    # #replace this
    # lyric_rows = lyric_rows.to_frame()
    # lyric_rows.to_csv(f_name, header=None, index=None, sep=' ',
    #  mode='a',encoding = 'utf_8') #quoting = csv.QUOTE_NONE

    #collapse strings into one strings
    # Series
    lines = lyric_rows.str.cat(sep='. ')

    # sentiment analyze each song
    blob = TextBlob(lines)
    feels = [w.sentiment for w in blob.sentences]
    filt = list(filter(lambda x: x.sentiment[0]!=0, blob.sentences))
    pos = len(list(filter(lambda x: x.sentiment[0]>0, filt)))
    neg = len(list(filter(lambda x: x.sentiment[0]<0, filt)))
    feels_score = sum([w.sentiment[0]*w.sentiment[1] for w in filt])/len(filt)
    #weighted avg of polarity and subjectivity

    #boost differences
    if (pos > neg):
        feels_score = feels_score * (pos/neg)
    elif (neg < pos):
        feels_score = feels_score * (neg/pos)

    if (feels_score > 0):
        #add to pos set
    elif (feels_score < 0):
        #add to neg set











# train model on positive songs


# train another model on negative songs


# write pos and neg songs!
