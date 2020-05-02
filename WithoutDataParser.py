import os
from pydub import AudioSegment

dir_data = './without_data/'
list_data = os.listdir(dir_data)


def wav_combine(file1, file2, export_name):
    sounds = [AudioSegment.from_wav(file1), AudioSegment.from_wav(file2)]
    playlist = AudioSegment.empty()
    for sound in sounds:
        # add into playlist
        playlist += sound
    playlist.export(export_name, format="mp3")
    print('Export finished:', export_name, '\n', file1, file2)


for k in list_data:
    if '_loop' in k:
        continue
    else:
        replaced_name = k.replace('_intro', '_loop')
        target_name = k.replace('_intro', '_combine').replace('.wav', '.mp3')
        wav_combine(dir_data + k, dir_data + replaced_name, dir_data + target_name)
