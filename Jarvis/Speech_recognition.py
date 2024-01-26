import speech_recognition as sr

def recognize_speech():
    # Create a recognizer instance
    recognizer = sr.Recognizer()

    # Capture audio from the microphone
    with sr.Microphone() as source:
        print("Say something:")
        try:
            # If you comment the below source code, the program will hang at this line.
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Error connecting to Google Web Speech API: {e}")
        finally:
            print('Speech complete.')

    try:
        # Recognize speech using Google Web Speech API
        text = recognizer.recognize_google(audio)
        #text = recognizer.recognize_sphinx(audio)

        print(f"You said: {text}")
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Error connecting to Google Web Speech API: {e}")

if __name__ == "__main__":
    recognize_speech()
