# Voice Activity Detection (VAD) with Silero

This project provides a simple yet effective tool for Voice Activity Detection (VAD) – identifying the presence or absence of human speech in an audio file. It leverages the highly accurate, pre-trained **Silero VAD** model.

## Features

- **Accurate Speech Detection**: Powered by Silero VAD, which boasts enterprise-grade accuracy.
- **Timestamp Extraction**: Returns precise start and end timestamps (in seconds) for detected speech segments.
- **Visualization**: Generates an intuitive timeline plot of the speech activity using Matplotlib.
- **Command-line Interface**: Easy to run on any audio file via simple CLI arguments.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/sahilgupta630/VAD-Audio-Detection.git
   cd VAD-Audio-Detection
   ```

2. (Optional but recommended) Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Simply run the Python script `vad_audio_detection.py` and pass the path to your audio file. 

```bash
python vad_audio_detection.py --audio path/to/your/audio_file.wav
```

If no audio file is provided, the script will default to looking for `Recording.m4a` in the base directory.

### Example Output

```text
Loading Silero VAD model...
Reading audio file: Recording.m4a
Detecting speech timestamps...
Speech Timestamps: [{'start': 1.2, 'end': 4.5}, {'start': 6.0, 'end': 9.3}]
```

A Matplotlib window will also pop up showing a timeline visualization of the spoken audio segments.

## Jupyter Notebook
Alternatively, you can explore the code interactively using the provided Jupyter Notebook: `VAD_Audio_Detection.ipynb`. It contains the original experiment flow and Google Colab compatibility.

## Acknowledgements

* [Silero VAD](https://github.com/snakers4/silero-vad) for the incredible and completely open-source VAD model constraint.
