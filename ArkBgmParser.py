import json

from ArkBgm.AudioComponent import *

dir_conf = './config/'

with open(f"{dir_conf}audio_data.json", encoding='utf-8') as f:
    bgmData = json.load(f)['bgmBanks']

for i in bgmData:
    intro_file = i['intro'].lower() + '.wav'

    try:
        loop_file = i['loop'].lower() + '.wav'
    except (TypeError, AttributeError) as e:
        print(i, "\n", e)
    duration = i['delay'] * 1000
    export_name = i['intro'].replace('_intro', '_combine') + '.mp3'

    try:
        wav_combine(intro_file, loop_file, duration, export_name)
    except FileNotFoundError as e:
        print("File1:", intro_file, "File2:", loop_file, e)
