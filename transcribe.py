import os
import pathlib
import sys
import threading

import whisper


INFOLDER = "./samples"
OUTFOLDER = "./transcriptions"
MODEL = "base.en"

# create OS paths for the input/output folders
input_folder: pathlib.Path = pathlib.Path(INFOLDER)
output_folder: pathlib.Path = pathlib.Path(OUTFOLDER)

    
def transcribe(file: pathlib.Path, index: int) -> None:
    file_name = str(file.resolve())
    print(f'Transcribing {file_name}')
    
    model: whisper.Whisper = whisper.load_model(MODEL)
    result = model.transcribe(file_name)
    out_file = output_folder / f'transcription{index}.txt'
    with open(out_file, 'w') as f:
        f.write(result["text"])


def main() -> None:
    threads: list[threading.Thread] = []

    # checks to make sure input folder exists
    if not os.path.exists(input_folder):
        print(f'Input folder {input_folder} does not exist.', file=sys.stderr)
        exit()

    # if the folder does not exist we create it
    if not os.path.exists(output_folder):
        print(f'Output folder {output_folder} does not exist, creating it.')
        os.makedirs(output_folder)

    # for each file, transcribe it and write it out to a text file
    for i, file in enumerate(input_folder.iterdir(), start=1):
        thr = threading.Thread(target=transcribe, args=(file, i))
        threads.append(thr)
        
    for thr in threads:
        thr.start()
        
    for thr in threads:
        thr.join()

if __name__ == '__main__':
    main()
    