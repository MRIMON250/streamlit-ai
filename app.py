import streamlit as st
from api import note_generator,audio_transcription,quiz_generation
from PIL import Image

st.title("Note Summary and Quiz Generator")
st.markdown("Upload upto 3 imagess to generate Note summary and Quizzes ")
st.divider()



with st.sidebar:
    st.header("Controls")
    #img
    images = st.file_uploader(
        "Upload the photos of your notes",
        type=['jpg','png','jpeg'],
        accept_multiple_files=True
    )

    pil_images =[]

    for img in images:
        pil_img = Image.open(img)
        pil_images.append(pil_img)

    if images:
        if len(images) > 3:
            st.error("Upload at max 3 imagees")
        else:
            st.subheader("Uploaded images")
            col = st.columns(len(images))
        
            for i,img in enumerate(images):
                with col[i]:
                    st.image(img)
    #difficulty
    selected_option = st.selectbox(
        "Enter the diffkculty of you quiz",
        ("Easy","meidium","Hard"),
        index = None
    )


    pressed = st.button("Click the button to initiate AI",type="primary")



if pressed:
    if not images:
        st.error("You must upload 1 image")
    if not selected_option:
        st.error("yoou must select a difficulty")

    if images and selected_option :

        #note
        with st.container(border=True):
            st.subheader("your note")
                # the  line will be replaced by ai api
            with st.spinner("Ai is writing notes for you"):
                generated_notes = note_generator(pil_images)
                st.text(generated_notes)

        #Audio
        with st.container(border=True):
            st.subheader("Audio Transcrition")
                # the  line will be replaced by ai api
            with st.spinner("Ai is generating audion transcripton for you"):
                audio_transcript = audio_transcription(generated_notes)
                st.audio(audio_transcript)
            
           
        #quiz
        with st.container(border=True):
            st.subheader(f"Quiz({selected_option}) Difficulty")
                # the  line will be replaced by ai api
        with st.spinner("Ai is writing Quiz for you"):
            quizzes = quiz_generation(pil_images,selected_option)
            st.markdown(quizzes)