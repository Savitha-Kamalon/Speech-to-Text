import streamlit as st
import whisper
import tempfile as tf
import os

st.title("Whisper App")
# upload audio file with streamlit
audio_file = st.file_uploader("Upload Audio",type=["wav","mp3","m4a","ogg"])

model = whisper.load_model("base")
#st.text("Whisper model loaded")

if audio_file is not None:
    st.sidebar.header("Play original Audio file")
    st.sidebar.audio(audio_file)
    #st.sidebar.audio(tmp_file.read(), format='audio/ogg')
    if st.sidebar.button("Transcribe Audio"):
        # Create a temporary file
        tmp_file = tf.NamedTemporaryFile(delete=False)  
         # Write audio content to the temporary file
        tmp_file.write(audio_file.read())
           
        st.sidebar.success("Transcribing Audio")
        transcription = model.transcribe(tmp_file.name)
        st.sidebar.success("Transcription Complete")
        st.markdown(transcription["text"])
        # Close the temporary file
        tmp_file.close()
        
        if tmp_file is not None:
            os.unlink(tmp_file.name)
else:
    st.sidebar.error("Please upload an audio file")





