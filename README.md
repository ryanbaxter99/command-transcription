# command-transcription
A tool to quickly transcribe multiple MP4 files then clean with chatGPT


## Installation

Create a virtual environment and activate it:
```bash
$ python3 -m venv env
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
