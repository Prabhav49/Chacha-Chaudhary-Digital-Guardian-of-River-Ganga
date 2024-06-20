<<<<<<< HEAD
import streamlit as st
from main import genai_engine
from streamlit_navigation_bar import st_navbar
import os
import speech_recognition as sr
import pyttsx3
from googletrans import Translator
import streamlit.components.v1 as components
from gtts import gTTS
import pygame
import random
import string

# Set page configuration
st.set_page_config(
    page_title='Chacha Chaudhary: The Digital Guardian of Namami Gange',
    page_icon='C:\\Users\\nihar\\Downloads\\professor.png',
    layout="wide"
)


# Apply CSS

parent_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(parent_dir, "logo.svg")

text = ["Chacha Chaudhary: The Digital Guardian of Namami Gange"]
styles = {
    "nav": {
        "background-image": "linear-gradient(135deg, #fefefe 0%, #00a4e4 100%)",
        "justify-content": "left",
        "height": "90px",
    },
    "img": {
        "padding-right": "8px",
        "height": "85px",
        "width": "275px",
    },
    "span": {
        "color": "#000080",
        "font-size": "36px",
        "width": "270%",
        "font-weight":"730",
        "font-family": "Georgia",
    },
    "active": {
        "color": "#000080",
        "font-size": "36px",
        "width": "270%",
        "font-weight":"730",
        "font-family": "Georgia",
    }
}
options = {
    "show_menu": False,
    "show_sidebar": False,
}

page = st_navbar(
    text,
    logo_path=logo_path,
    styles=styles,
    options=options,
)

# Create two columns for the layout
col1, col2 = st.columns([1, 3])

# SECTION SLIDEBAR STARTED
# Define the carousel items
with col1:
    test_items = [
        dict(
            title="Slide 1",
            text="A tree in the savannah",
            img="https://img.freepik.com/free-photo/wide-angle-shot-single-tree-growing-clouded-sky-during-sunset-surrounded-by-grass_181624-22807.jpg?w=1380&t=st=1688825493~exp=1688826093~hmac=cb486d2646b48acbd5a49a32b02bda8330ad7f8a0d53880ce2da471a45ad08a4",
            link="https://discuss.streamlit.io/t/new-component-react-bootstrap-carousel/46819"
        ),
        dict(
            title="Slide 2",
            text="A wooden bridge in a forest in Autumn",
            img="https://img.freepik.com/free-photo/beautiful-wooden-pathway-going-breathtaking-colorful-trees-forest_181624-5840.jpg?w=1380&t=st=1688825780~exp=1688826380~hmac=dbaa75d8743e501f20f0e820fa77f9e377ec5d558d06635bd3f1f08443bdb2c1",
            link="https://github.com/thomasbs17/streamlit-contributions/tree/master/bootstrap_carousel"
        ),
        dict(
            title="Slide 3",
            text="A distant mountain chain preceded by a sea",
            img="https://img.freepik.com/free-photo/aerial-beautiful-shot-seashore-with-hills-background-sunset_181624-24143.jpg?w=1380&t=st=1688825798~exp=1688826398~hmac=f623f88d5ece83600dac7e6af29a0230d06619f7305745db387481a4bb5874a0",
            link="https://github.com/thomasbs17/streamlit-contributions/tree/master"
        ),
    ]

    # Generate the HTML for the carousel
    def generate_carousel_html(items):
        indicators = "".join(
            f'<li data-target="#carouselExampleIndicators" data-slide-to="{i}" class="{"active" if i == 0 else ""}"></li>'
            for i in range(len(items))
        )
        
        slides = "".join(
            f'''
            <div class="carousel-item {"active" if i == 0 else ""}">
                <a href="{item["link"]}" target="_blank">
                    <img src="{item["img"]}" class="d-block w-100" alt="{item["title"]}">
                    <div class="carousel-caption d-none d-md-block">
                        <h5>{item["title"]}</h5>
                        <p>{item["text"]}</p>
                    </div>
                </a>
            </div>
            '''
            for i, item in enumerate(items)
        )
        
        html = f'''
        <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel" style="width: 100%;">
            <ol class="carousel-indicators">
                {indicators}
            </ol>
            <div class="carousel-inner">
                {slides}
            </div>
            <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="sr-only">Previous</span>
            </a>
            <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="sr-only">Next</span>
            </a>
        </div>
        '''
        return html

    # Include Bootstrap CSS and JS
    bootstrap_cdn = '''
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
    '''

    # Generate the full HTML for the page
    html = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        {bootstrap_cdn}
        <title>Carousel</title>
    </head>
    <body>
        {generate_carousel_html(test_items)}
    </body>
    </html>
    '''

    # Display the carousel in Streamlit
    components.html(html, height=600)

# CHATBOT SECTION STARTED
with col2:
    st.header(" :blue[_Chacha Chaudhary's Gange Guide !_]", divider='rainbow')

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Function for voice recognition
    def recognize_speech():
        recognizer = sr.Recognizer()
        status_text = st.empty()  # Placeholder for status message
        status_text.write("Chacha Chaudhary is all ears...")
        with sr.Microphone() as source:
            audio = recognizer.listen(source)
            status_text.write("Chacha Chaudhary is consulting his turban of wisdom...")
        try:
            query = recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            status_text.write("Sorry, I could not understand what you said.")
            query = ""
        finally:
            # Remove the status message
            status_text.empty()
        return query

    # Function for text-to-speech
    def generate_random_string(length=6):
        """Generate a random string of lowercase letters and digits."""
        letters_and_digits = string.ascii_lowercase + string.digits
        return ''.join(random.choice(letters_and_digits) for _ in range(length))

    def text_to_speech(text, speed=150, language='en'):
        engine = None  # Initialize engine variable
        
        if language != 'hi':
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            engine.setProperty('rate', speed)

            # Selecting a voice for the specified language
            for voice in voices:
                if language.lower() in voice.languages:
                    engine.setProperty('voice', voice.id)
                    break

            engine.say(text)
            engine.runAndWait()

        # else:
        #     # Initialize engine for the else block
        #     engine = pyttsx3.init()
            
        #     # Convert text to Hindi speech using gTTS
        #     tts = gTTS(text=text, lang=language)
            
        #     # Specify the directory where you want to save the file
        #     parent_dir = os.path.dirname(os.path.abspath(__file__))
        #     output_dir = os.path.join(parent_dir, "Output_voices")
        #     if not os.path.exists(output_dir):
        #         os.makedirs(output_dir)
            
        #     output_file = os.path.join(output_dir, f"output_{generate_random_string()}.mp3")  # Unique filename
        #     tts.save(output_file)

        #     # Initialize pygame mixer
        #     pygame.mixer.init()
            
        #     pygame.mixer.music.load(output_file)
        #     pygame.mixer.music.play()
  

    # Function to detect language
    def detect_language(text):
        translator = Translator()
        return translator.detect(text).lang

    # Function to translate text
    def translate_text(text, dest_lang):
        translator = Translator()
        return translator.translate(text, dest_lang).text

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        if message["role"] == "user":
            with st.chat_message("user"):
                st.markdown(message["content"])
        elif message["role"] == "assistant":
            st.write('<style>div.Widget.row-widget.stHorizontal</style>', unsafe_allow_html=True)
            col1, col2 = st.columns([1, 10])
            with col1:
                st.image("E:\\Chacha\\chacha_small.png", width=50)
            with col2:
                st.markdown(message["content"])

    # Add button for voice input
    if st.button("Speak"):
        prompt = recognize_speech()
        if prompt:
            user_lang = detect_language(prompt)
            
            if user_lang != 'en':
                disp_input = translate_text(prompt, 'hi')
            else:
                disp_input = prompt

            st.chat_message("user").markdown(disp_input)

            # Add user message to chat history with detected language
            st.session_state.messages.append({"role": "user", "content": disp_input, "language": user_lang})

            # Translate to English if not already in English
            if user_lang != 'en':
                prompt = translate_text(prompt, 'en')

            # Create a placeholder for the assistant's response
            response_placeholder = st.empty()
            response_placeholder.markdown("")

            if user_lang != 'hi':
                with st.spinner("Chacha Chaudhary is crafting a clever response..."):
                    response = genai_engine(prompt)
            else : 
                with st.spinner("चाचा चौधरी का दिमाग कंप्यूटर से भी तेज़ चल रहा है..."):
                    response = genai_engine(prompt)

            # Translate response back to user's language if it was not English
            if user_lang == 'hi':
                response = translate_text(response, 'hi')

            # Display assistant response and image in a horizontal layout
            st.write('<style>div.Widget.row-widget.stHorizontal</style>', unsafe_allow_html=True)
            col1, col2 = st.columns([1, 10])
            with col1:
                st.image("E:\\Chacha\\chacha_small.png", width=50)
            with col2:
                response_placeholder.markdown(response)

            # Add assistant response to chat history with response language
            st.session_state.messages.append({"role": "assistant", "content": response, "language": user_lang})

            # Convert text response to speech
            text_to_speech(response, speed=150, language=user_lang)

    # React to user input
    if prompt := st.chat_input("What is up?"):
        user_lang = detect_language(prompt)
        
        if user_lang != 'en':
            disp_input = translate_text(prompt, 'hi')
        else:
            disp_input = prompt

        st.chat_message("user").markdown(disp_input)

        # Add user message to chat history with detected language
        st.session_state.messages.append({"role": "user", "content": disp_input, "language": user_lang})

        # Translate to English if not already in English
        if user_lang != 'en':
            prompt = translate_text(prompt, 'en')

        # Create a placeholder for the assistant's response
        response_placeholder = st.empty()
        response_placeholder.markdown("")

        if user_lang != 'hi':
            with st.spinner("Chacha Chaudhary is crafting a clever response..."):
                response = genai_engine(prompt)
        else : 
            with st.spinner("चाचा चौधरी का दिमाग कंप्यूटर से भी तेज़ चल रहा है..."):
                response = genai_engine(prompt)

        # Translate response back to user's language if it was not English
        if user_lang == 'hi':
            response = translate_text(response, 'hi')

        # Display assistant response and image in a horizontal layout
        st.write('<style>div.Widget.row-widget.stHorizontal</style>', unsafe_allow_html=True)
        col1, col2 = st.columns([1, 10])
        with col1:
            st.image("E:\\Chacha\\chacha_small.png", width=50)
        with col2:
            response_placeholder.markdown(response)

        # Add assistant response to chat history with response language
        st.session_state.messages.append({"role": "assistant", "content": response, "language": user_lang})

        # Convert text response to speech
=======
import streamlit as st
from main import genai_engine
from streamlit_navigation_bar import st_navbar
import os
import speech_recognition as sr
import pyttsx3
from googletrans import Translator
import streamlit.components.v1 as components
from gtts import gTTS
import pygame
import random
import string

# Set page configuration
st.set_page_config(
    page_title='Chacha Chaudhary: The Digital Guardian of Namami Gange',
    page_icon='C:\\Users\\nihar\\Downloads\\professor.png',
    layout="wide"
)


# Apply CSS

parent_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(parent_dir, "logo.svg")

text = ["Chacha Chaudhary: The Digital Guardian of Namami Gange"]
styles = {
    "nav": {
        "background-image": "linear-gradient(135deg, #fefefe 0%, #00a4e4 100%)",
        "justify-content": "left",
        "height": "90px",
    },
    "img": {
        "padding-right": "8px",
        "height": "85px",
        "width": "275px",
    },
    "span": {
        "color": "#000080",
        "font-size": "36px",
        "width": "270%",
        "font-weight":"730",
        "font-family": "Georgia",
    },
    "active": {
        "color": "#000080",
        "font-size": "36px",
        "width": "270%",
        "font-weight":"730",
        "font-family": "Georgia",
    }
}
options = {
    "show_menu": False,
    "show_sidebar": False,
}

page = st_navbar(
    text,
    logo_path=logo_path,
    styles=styles,
    options=options,
)

# Create two columns for the layout
col1, col2 = st.columns([1, 3])

# SECTION SLIDEBAR STARTED
# Define the carousel items
with col1:
    test_items = [
        dict(
            title="Slide 1",
            text="A tree in the savannah",
            img="https://img.freepik.com/free-photo/wide-angle-shot-single-tree-growing-clouded-sky-during-sunset-surrounded-by-grass_181624-22807.jpg?w=1380&t=st=1688825493~exp=1688826093~hmac=cb486d2646b48acbd5a49a32b02bda8330ad7f8a0d53880ce2da471a45ad08a4",
            link="https://discuss.streamlit.io/t/new-component-react-bootstrap-carousel/46819"
        ),
        dict(
            title="Slide 2",
            text="A wooden bridge in a forest in Autumn",
            img="https://img.freepik.com/free-photo/beautiful-wooden-pathway-going-breathtaking-colorful-trees-forest_181624-5840.jpg?w=1380&t=st=1688825780~exp=1688826380~hmac=dbaa75d8743e501f20f0e820fa77f9e377ec5d558d06635bd3f1f08443bdb2c1",
            link="https://github.com/thomasbs17/streamlit-contributions/tree/master/bootstrap_carousel"
        ),
        dict(
            title="Slide 3",
            text="A distant mountain chain preceded by a sea",
            img="https://img.freepik.com/free-photo/aerial-beautiful-shot-seashore-with-hills-background-sunset_181624-24143.jpg?w=1380&t=st=1688825798~exp=1688826398~hmac=f623f88d5ece83600dac7e6af29a0230d06619f7305745db387481a4bb5874a0",
            link="https://github.com/thomasbs17/streamlit-contributions/tree/master"
        ),
    ]

    # Generate the HTML for the carousel
    def generate_carousel_html(items):
        indicators = "".join(
            f'<li data-target="#carouselExampleIndicators" data-slide-to="{i}" class="{"active" if i == 0 else ""}"></li>'
            for i in range(len(items))
        )
        
        slides = "".join(
            f'''
            <div class="carousel-item {"active" if i == 0 else ""}">
                <a href="{item["link"]}" target="_blank">
                    <img src="{item["img"]}" class="d-block w-100" alt="{item["title"]}">
                    <div class="carousel-caption d-none d-md-block">
                        <h5>{item["title"]}</h5>
                        <p>{item["text"]}</p>
                    </div>
                </a>
            </div>
            '''
            for i, item in enumerate(items)
        )
        
        html = f'''
        <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel" style="width: 100%;">
            <ol class="carousel-indicators">
                {indicators}
            </ol>
            <div class="carousel-inner">
                {slides}
            </div>
            <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="sr-only">Previous</span>
            </a>
            <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="sr-only">Next</span>
            </a>
        </div>
        '''
        return html

    # Include Bootstrap CSS and JS
    bootstrap_cdn = '''
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
    '''

    # Generate the full HTML for the page
    html = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        {bootstrap_cdn}
        <title>Carousel</title>
    </head>
    <body>
        {generate_carousel_html(test_items)}
    </body>
    </html>
    '''

    # Display the carousel in Streamlit
    components.html(html, height=600)

# CHATBOT SECTION STARTED
with col2:
    st.header(" :blue[_Chacha Chaudhary's Gange Guide !_]", divider='rainbow')

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Function for voice recognition
    def recognize_speech():
        recognizer = sr.Recognizer()
        status_text = st.empty()  # Placeholder for status message
        status_text.write("Chacha Chaudhary is all ears...")
        with sr.Microphone() as source:
            audio = recognizer.listen(source)
            status_text.write("Chacha Chaudhary is consulting his turban of wisdom...")
        try:
            query = recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            status_text.write("Sorry, I could not understand what you said.")
            query = ""
        finally:
            # Remove the status message
            status_text.empty()
        return query

    # Function for text-to-speech
    def generate_random_string(length=6):
        """Generate a random string of lowercase letters and digits."""
        letters_and_digits = string.ascii_lowercase + string.digits
        return ''.join(random.choice(letters_and_digits) for _ in range(length))

    def text_to_speech(text, speed=150, language='en'):
        engine = None  # Initialize engine variable
        
        if language != 'hi':
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            engine.setProperty('rate', speed)

            # Selecting a voice for the specified language
            for voice in voices:
                if language.lower() in voice.languages:
                    engine.setProperty('voice', voice.id)
                    break

            engine.say(text)
            engine.runAndWait()

        # else:
        #     # Initialize engine for the else block
        #     engine = pyttsx3.init()
            
        #     # Convert text to Hindi speech using gTTS
        #     tts = gTTS(text=text, lang=language)
            
        #     # Specify the directory where you want to save the file
        #     parent_dir = os.path.dirname(os.path.abspath(__file__))
        #     output_dir = os.path.join(parent_dir, "Output_voices")
        #     if not os.path.exists(output_dir):
        #         os.makedirs(output_dir)
            
        #     output_file = os.path.join(output_dir, f"output_{generate_random_string()}.mp3")  # Unique filename
        #     tts.save(output_file)

        #     # Initialize pygame mixer
        #     pygame.mixer.init()
            
        #     pygame.mixer.music.load(output_file)
        #     pygame.mixer.music.play()
  

    # Function to detect language
    def detect_language(text):
        translator = Translator()
        return translator.detect(text).lang

    # Function to translate text
    def translate_text(text, dest_lang):
        translator = Translator()
        return translator.translate(text, dest_lang).text

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        if message["role"] == "user":
            with st.chat_message("user"):
                st.markdown(message["content"])
        elif message["role"] == "assistant":
            st.write('<style>div.Widget.row-widget.stHorizontal</style>', unsafe_allow_html=True)
            col1, col2 = st.columns([1, 10])
            with col1:
                st.image("E:\\Chacha\\chacha_small.png", width=50)
            with col2:
                st.markdown(message["content"])

    # Add button for voice input
    if st.button("Speak"):
        prompt = recognize_speech()
        if prompt:
            user_lang = detect_language(prompt)
            
            if user_lang != 'en':
                disp_input = translate_text(prompt, 'hi')
            else:
                disp_input = prompt

            st.chat_message("user").markdown(disp_input)

            # Add user message to chat history with detected language
            st.session_state.messages.append({"role": "user", "content": disp_input, "language": user_lang})

            # Translate to English if not already in English
            if user_lang != 'en':
                prompt = translate_text(prompt, 'en')

            # Create a placeholder for the assistant's response
            response_placeholder = st.empty()
            response_placeholder.markdown("")

            if user_lang != 'hi':
                with st.spinner("Chacha Chaudhary is crafting a clever response..."):
                    response = genai_engine(prompt)
            else : 
                with st.spinner("चाचा चौधरी का दिमाग कंप्यूटर से भी तेज़ चल रहा है..."):
                    response = genai_engine(prompt)

            # Translate response back to user's language if it was not English
            if user_lang == 'hi':
                response = translate_text(response, 'hi')

            # Display assistant response and image in a horizontal layout
            st.write('<style>div.Widget.row-widget.stHorizontal</style>', unsafe_allow_html=True)
            col1, col2 = st.columns([1, 10])
            with col1:
                st.image("E:\\Chacha\\chacha_small.png", width=50)
            with col2:
                response_placeholder.markdown(response)

            # Add assistant response to chat history with response language
            st.session_state.messages.append({"role": "assistant", "content": response, "language": user_lang})

            # Convert text response to speech
            text_to_speech(response, speed=150, language=user_lang)

    # React to user input
    if prompt := st.chat_input("What is up?"):
        user_lang = detect_language(prompt)
        
        if user_lang != 'en':
            disp_input = translate_text(prompt, 'hi')
        else:
            disp_input = prompt

        st.chat_message("user").markdown(disp_input)

        # Add user message to chat history with detected language
        st.session_state.messages.append({"role": "user", "content": disp_input, "language": user_lang})

        # Translate to English if not already in English
        if user_lang != 'en':
            prompt = translate_text(prompt, 'en')

        # Create a placeholder for the assistant's response
        response_placeholder = st.empty()
        response_placeholder.markdown("")

        if user_lang != 'hi':
            with st.spinner("Chacha Chaudhary is crafting a clever response..."):
                response = genai_engine(prompt)
        else : 
            with st.spinner("चाचा चौधरी का दिमाग कंप्यूटर से भी तेज़ चल रहा है..."):
                response = genai_engine(prompt)

        # Translate response back to user's language if it was not English
        if user_lang == 'hi':
            response = translate_text(response, 'hi')

        # Display assistant response and image in a horizontal layout
        st.write('<style>div.Widget.row-widget.stHorizontal</style>', unsafe_allow_html=True)
        col1, col2 = st.columns([1, 10])
        with col1:
            st.image("E:\\Chacha\\chacha_small.png", width=50)
        with col2:
            response_placeholder.markdown(response)

        # Add assistant response to chat history with response language
        st.session_state.messages.append({"role": "assistant", "content": response, "language": user_lang})

        # Convert text response to speech
>>>>>>> 32e84ee0b39b60a128c7cace587dd13adbfd2aae
        text_to_speech(response, speed=150, language=user_lang)