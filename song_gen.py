import sys
import markovify
import json
import random
from watson_developer_cloud import TextToSpeechV1
from watson_developer_cloud import WatsonApiException

try:
    artist = str(sys.argv[1])
    song_name = str(sys.argv[2])
    gender = str(sys.argv[3])
except:
    print("Not enough args")
    exit()

m_file = './models/'+artist+'.json'
try:
    with open(m_file) as f:
        json_file = json.load(f)
except:
    print("File not found")
    exit()

text_model = markovify.Text.from_json(json_file)

# Print three randomly-generated sentences of no more than 140 characters
num_lines = random.choice([20,25,30])
new_song = ''
for i in range(num_lines):
    new_song += (text_model.make_short_sentence(100) + '\n')
    if(i !=0 and i % 5 == 0):
        new_song+='\n'

# TODO: most frequent word is title
print(new_song)

f_name = './new_lyrics/'+artist+'_'+song_name+'.txt'
new_f = open(f_name, 'w')
new_f.write(new_song)
new_f.close()

#text to speech!
text_to_speech = TextToSpeechV1(
    username='3fe8faa7-2f2f-4532-be16-7ab6cdaab1d8',
    password='4ZXb4LqniSxN',
    url='https://stream.watsonplatform.net/text-to-speech/api'
)

if gender == 'f':
    voice = 'en-US_AllisonVoice'
else:
    voice = 'en-US_MichaelVoice'

s_name = './mp3_files/'+artist+'_'+song_name+'.mp3'
with open(s_name, 'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(
            new_song,
            'audio/mp3',
            voice
        ).get_result().content)

# TODO: incorporate background music library
