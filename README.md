# Audio to Text Conversion with OpenAI's Whisper
Whisper is a speech-to-text API developed by OpenAI. The API can transcribe spoken words in real-time and return the text as an output. The goal of this project is to create a simple web application that allows users to upload an audio file and use the Whisper API to transcribe the audio to text.

The user will be able to upload an audio file, which will be temporarily stored on the server. The user will then be able to click a button to initiate the transcription process. The application will use the OpenAI Whisper API to convert the audio to text, which will be displayed to the user in real-time.

The application will be developed using the Streamlit library, which is a Python-based open-source framework for building data-centric web applications. The final application will be user-friendly and allow users to easily convert audio files to text with the click of a button.
# Prerequisites
1. python 3.9 or higher
2. [Github](https://github.com/)
3. [VS Code](https://code.visualstudio.com/)

# setup
1. brew install ffmpeg    
2. conda install pytorch torchvision torchaudio -c pytorch
3. pip install git+https://github.com/openai/whisper.git 


# Usage
1. Run the Streamlit app: streamlit run app.py.
2. Use the file uploader to select an audio file (mp3, wav or flac).
3. Click on the "Transcribe" button to start the transcription process.
4. Wait for the transcription to complete (it may take a few seconds).
5. The transcribed text will be displayed on the screen.
