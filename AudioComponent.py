from pydub import AudioSegment


def customSilentAudio(duration):
    return AudioSegment.silent(duration=duration)


def wav_combine(file1, file2, delay, export_name):
    if delay != 0.0:
        sounds = [AudioSegment.from_wav(file1), customSilentAudio(delay), AudioSegment.from_wav(file2)]
        # test = AudioSegment.empty()
        # test += customSilentAudio(delay)
        # test.export('test.mp3', format="mp3")
        # print('sth')
    else:
        sounds = [AudioSegment.from_wav(file1), AudioSegment.from_wav(file2)]
    playlist = AudioSegment.empty()
    for sound in sounds:
        playlist += sound
    playlist.export(export_name, format="mp3")
    print('Export finished:', export_name)
    print(f"|-{file1}", file2, delay)