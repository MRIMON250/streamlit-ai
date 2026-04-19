from google import genai
from dotenv import load_dotenv
import os
from PIL import Image
from gtts import gTTS
import io

#loading the enviranment veeriabole
load_dotenv()

my_api_key = os.getenv("GEMINI_API_KEY")

#initializing a client
client = genai.Client(api_key= my_api_key)



#note generator
def note_generator(images):

    prompt = """Summarize the picture in note format in 
    language Bangla at max 100 words
    make sure to add necessary markdown to differentiate 
    different section"""    

    response = client.models.generate_content(
        model= "gemini-3-flash-preview",
        contents=[images,prompt]
    )

    return response.text


def audio_transcription(text):
    speech = gTTS(text,lang='en',slow=False)
    # speech.save("welcome.mp3")
    audio_buffer = io.BytesIO()
    speech.write_to_fp(audio_buffer)

    return(audio_buffer)

def quiz_generation(image,difficulty):

    prompt = f"""Generate 3 quizzes based on the {difficulty}.
      Make sure to add markdown to differentiate the options. Add correct answer too,after the quiz"""

    response = client.models.generate_content(
        model= "gemini-3-flash-preview",
        contents=[image,prompt]
    )

    return response.text