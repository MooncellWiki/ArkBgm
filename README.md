# ArkBgm
A tool to merge the background music of Arknights into one file.

## Requirements
- pydub
- json

## Usage
1. Export wav files from ab files and copy to <code>/audio/</code>.<br>
	**IMPORTANT:** Files should be exported in the format of the definition in audio_data.
2. Place the audio_data.json into <code>/config/</code>.
3. Run <code>ArkBgmParser.py</code>.<br/>
	**If there are files aren't included in the data:**
	>1. Place the non-definition .wav files into <code>/without_data/</code>.
	>2. Run <code>WithoutDataParser.py</code>.
4. Check *_combine.wav files in <code>/audio/</code> or <code>/without_data/</code>. (Use Search)
