# ArkBgm
A tool to merge the Background music of Arknights into one file.

## Requirements
- pydub
- json

## Usage
1. Export wav files from ab files and copy to the root directory.

	**IMPORTANT:** Files should be exported as the format of the definition in audio_data.
2. Run ArkBgmParser.py.
	If there are files which are not included in the data, use WithoutDataParser.py.
3. Check *_combine.wav files in /audio (Use Search)
