# -*- coding: utf-8 -*-

import os
import glob
import argparse
import whisper
import re

def transcribe_using_whisper(input_file, output_file, model="small", verbose=False, language="ja"):
    model = whisper.load_model(model)
    result = model.transcribe(input_file, verbose=verbose, language=language)

    with open(output_file, 'a', encoding='utf-8') as f:  # 'a' mode for appending, and set encoding to utf-8
        f.write(f"\n--- Transcription for {os.path.basename(input_file)} ---\n")  # print the input filename
        for section in re.split('[、。]', result['text']):  # split the text into sections by "、" or "。"
            f.write(section.strip() + '\n')  # add a newline character after each section

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert audio files in a directory to text using whisper")
    parser.add_argument("input_directory", help="Path to input directory containing audio files")
    args = parser.parse_args()

    # strip trailing slash from directory if exists
    input_directory = args.input_directory.rstrip('/')

    output_file = f"{input_directory}.txt"  # create output file based on the directory name

    # if the output file already exists, remove it
    if os.path.exists(output_file):
        os.remove(output_file)

    for input_file in sorted(glob.glob(os.path.join(input_directory, '*.mp3'))):  # Sort the files
        transcribe_using_whisper(input_file, output_file)
