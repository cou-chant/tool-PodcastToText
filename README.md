# PodcastToText

PodcastToText is a Python script for converting audio files in a specific directory to text, using the Whisper ASR model.

## Requirements

- Python 3.7 or later
- Whisper ASR

## Installation

1. Install Whisper ASR according to its official instructions.

2. Clone this repository to your local machine.

## Usage

1. Run the script by using the following command:

```sh
python3 PodcastToText.py <input_directory>
```

Replace <input_directory> with the path to the directory containing the audio files you wish to transcribe.

The script will create a text file in the current directory with the same name as the directory, which will contain the transcriptions of the audio files.

## License

MIT License
