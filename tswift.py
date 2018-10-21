import sys
import markovify
import json
from watson_developer_cloud import TextToSpeechV1
from watson_developer_cloud import WatsonApiException

name = str(sys.argv[1])

# all_file = './tswift_songs/input.txt'
with open('./model_json.json') as f:
    json_file = json.load(f)

# Get raw text as string.
# with open(all_file) as f:
#     text = f.read()

# # Build the model.
# text_model = markovify.NewlineText(text)
# model_json = text_model.to_json()
# # print(model_json)

text_model = markovify.Text.from_json(json_file)
# Print three randomly-generated sentences of no more than 140 characters
new_song = ''
for i in range(20):
    new_song += (text_model.make_short_sentence(140) + '\n')
print(new_song)

f_name = './new_songs/tswift_'+name+'.txt'
new_f = open(f_name, 'w')
new_f.write(new_song)
new_f.close()

#text to speech!
text_to_speech = TextToSpeechV1(
    username='3fe8faa7-2f2f-4532-be16-7ab6cdaab1d8',
    password='4ZXb4LqniSxN',
    url='https://stream.watsonplatform.net/text-to-speech/api'
)

s_name = './song_files/tswift_'+name+'.wav'
with open(s_name, 'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(
            new_song,
            'audio/wav',
            'en-US_AllisonVoice'
        ).get_result().content)
