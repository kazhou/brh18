import sys
import pandas
import string
import re
import csv
from textblob import TextBlob
import markovify
import json
from watson_developer_cloud import TextToSpeechV1
from watson_developer_cloud import WatsonApiException

df = pandas.read_csv("taylor_swift_lyrics.csv", encoding = 'unicode_escape')
print(df)

print(df['track_title'].nunique()) #94 songs
titles = df['track_title'].unique()

#track name | lyrics
all_songs={}#{title:TextBlob of lyrics}
pos_songs={}#[None]*len(titles)
neg_songs={}

total_pos = 0
total_neg = 0
# write all songs to their own files,

all_file = './tswift_songs/input.txt'
# pos_file = './tswift_songs/positive.txt'
# neg_file = './tswift_songs/negative.txt'
# for song_index in range(len(titles)):
#     song = titles[song_index]
#     song = re.sub(r'[^\w\s]','',song) #remove
#     # song.strip(string.punctuation)
#
#     f_name = './tswift_songs/' + song +'.txt'
#     print(f_name)
#     # rows of lyrics of song 'song_index'
#     lyric_rows = df[df['track_title'] == titles[song_index]]['lyric']
#     #write all lyrics to tswift_songs directory
#
#     # for i in range(len(lyric_rows)):
#     #     lyric_rows[i] = re.sub(r'[^\"]',"'",lyric_rows[i]) #replace quotes
#
#     # #replace this
#     lyric_frame = lyric_rows.to_frame()
#     #appends to all_file
#     # lyric_frame.to_csv(all_file, header=None, index=None, sep=' ',
#     #  mode='a',encoding = 'utf_8') #quoting = csv.QUOTE_NONE
#
#     # collapse strings into one strings
#     # Series
#     lines = lyric_rows.str.cat(sep='. ')
#     markov_lines = lyric_rows.str.cat(sep='\n') #for markovify
#     markov_lines.strip(string.punctuation)
#     #
#     # sentiment analyze each song
#     blob = TextBlob(lines)
#
#     all_songs[song] = blob
#
#     feels = [w.sentiment for w in blob.sentences]
#     filt = list(filter(lambda x: x.sentiment[0]!=0, blob.sentences))
#     pos = len(list(filter(lambda x: x.sentiment[0]>0, filt)))
#     neg = len(list(filter(lambda x: x.sentiment[0]<0, filt)))
#     feels_score = sum([w.sentiment[0]*w.sentiment[1] for w in filt])/len(filt)
#     #weighted avg of polarity and subjectivity
#
#     #boost differences
#     # if (pos > neg):
#     #     feels_score = feels_score * ((pos+pos)/(pos+neg))
#     # elif (neg < pos):
#     #     feels_score = feels_score * ((neg+neg)/(pos+neg))
#
#     if (feels_score > 0):
#         #add to pos set
#         total_pos += 1
#         pos_songs[song] = blob
#         # file = open(pos_file,"a",encoding="utf-8")
#         # file.write(markov_lines)
#         # file.close()
#     elif (feels_score < 0):
#         #add to neg set
#         total_neg += 1
#         neg_songs[song] = blob
#         # file = open(neg_file,"a",encoding="utf-8")
#         # file.write(markov_lines)
#         # file.close()

#songs summary
# print(total_pos, total_neg) #65,29

# print(all_file)

# markov model?
# https://github.com/jsvine/markovify
# https://medium.com/ymedialabs-innovation/next-word-prediction-using-markov-model-570fc0475f96
# https://github.com/ashwinmj/word-prediction/blob/master/MarkovModel.ipynb

# Get raw text as string.
with open(all_file) as f:
    text = f.read()

# Build the model.
text_model = markovify.NewlineText(text)
model_json = text_model.to_json()
# print(model_json)
with open('./model_json.json', 'w') as outfile:
    json.dump(model_json, outfile)
# new_f = open(, 'w')
# new_f.write(model_json)
# new_f.close()


# Print three randomly-generated sentences of no more than 140 characters
new_song = ''
for i in range(20):
    new_song += (text_model.make_short_sentence(140) + '\n')
print(new_song)



# # train model on positive songs
# with open(pos_file) as p:
#     pos_text = p.read()
#
# # Build the model.
# pos_model = markovify.NewlineText(pos_text)
#
# # Print three randomly-generated sentences of no more than 140 characters
# for i in range(20):
#     print(pos_model.make_short_sentence(140))
#
#
#
# # train another model on negative songs
# with open(neg_file) as n:
#     neg_text = n.read()
#
# # Build the model.
# neg_model = markovify.NewlineText(neg_text)
#
# # Print three randomly-generated sentences of no more than 140 characters
# for i in range(20):
#     print(neg_model.make_short_sentence(140))

# write pos and neg songs!

#text to speech!
text_to_speech = TextToSpeechV1(
    username='3fe8faa7-2f2f-4532-be16-7ab6cdaab1d8',
    password='4ZXb4LqniSxN',
    url='https://stream.watsonplatform.net/text-to-speech/api'
)

with open('tswift.wav', 'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(
            new_song,
            'audio/wav',
            'en-US_AllisonVoice'
        ).get_result().content)
