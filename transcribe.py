"""Run a transcription on a folder of audio files.

Using OpenAI's Whisper library, this module reads from a folder
and transcribes each audio file to a corresponding text file.
"""
import argparse
import os
import sys
from pathlib import Path

import whisper

INFOLDER = "samples"
OUTFOLDER = "transcriptions"
MODEL = "base.en"


def handle_io(args: argparse.Namespace) -> tuple[Path, Path]:
    """Process and validate the input/output folders."""
    # process the input/output folders from argparse
    input_folder: Path = Path(args.input_folder).resolve()
    output_folder: Path = Path(args.output_folder).resolve()

    # checks to make sure input folder exists
    if not os.path.exists(input_folder):
        print(f'Input folder {input_folder} does not exist.', file=sys.stderr)
        sys.exit(1)

    # if the output folder does not exist we create it
    if not os.path.exists(output_folder):
        print(
            f'Output folder {output_folder.name} does not exist, creating it.')
        os.makedirs(output_folder)
    
   

    return input_folder, output_folder


def transcribe(model: whisper.Whisper, out_folder: Path, in_file: Path,
               index: int, verbose: bool) -> None:
    """Transcribe and write out the transcription to a text file."""
    # prepare input/output files
    in_file_name = str(in_file)
    out_file = out_folder / f'transcription{index}.txt'
    print(f'*** Transcribing {in_file.name} to {out_file.name} ***')

    # transcribe the file
    transcription = model.transcribe(in_file_name, verbose=verbose)

    # write out the transcription to a text file
    with open(out_file, 'w', encoding='utf-8') as file:
        file.write(transcription["text"])


def main() -> None:
    """Run the main entry point for the program."""
    argparser = argparse.ArgumentParser(description='Transcribe audio files.')
    argparser.add_argument('input_folder', nargs='?',
                           help='Input folder', default=INFOLDER)
    argparser.add_argument('output_folder', nargs='?',
                           help='Output folder', default=OUTFOLDER)
    argparser.add_argument('-v', '--verbose', action='store_true',
                           help='Run with verbose output')
    args = argparser.parse_args()

    # create OS paths for the input/output folders
    input_folder, output_folder = handle_io(args)

    # load the model to use
    model: whisper.Whisper = whisper.load_model(MODEL)

    # for each file, transcribe it and write it out to a text file
    for i, file in enumerate(input_folder.iterdir(), start=1):
        transcribe(model, output_folder, file.resolve(), i, args.verbose)


if __name__ == '__main__':
    main()
