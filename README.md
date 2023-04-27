# command-transcription
A tool to quickly transcribe multiple audio files and clean them with ChatGPT.


## Installation

Create a virtual environment and activate it:
```bash
$ python -m venv env
$ source env/bin/activate
```

Install the requirements:
```bash
$ pip install -r requirements.txt
```

Install ffmpeg (choose ONE):
```bash
# on Ubuntu or Debian
sudo apt update && sudo apt install ffmpeg

# on Arch Linux
sudo pacman -S ffmpeg

# on MacOS using Homebrew (https://brew.sh/)
brew install ffmpeg

# on Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg

# on Windows using Scoop (https://scoop.sh/)
scoop install ffmpeg
```

## Usage

Run the transcription script with Python. Use the `-h` flag to see the available options.
```bash
$ python transcribe.py <options>
```

Run the cleaning script with Python. The default input folder is `transcriptions`.
```bash
$ python clean.py
```
