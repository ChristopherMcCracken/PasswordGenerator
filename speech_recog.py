
import speech_recognition as sr
'''
Free API's to use for speech recognition
recognize_bing()
recognize_google()
recognize_google_cloud()
recognize_houndify()
recognize_ibm()
recognize_sphinx()
recognize_wit()

IMPORTANT: Speech recognition will not be used in our program, speech_recognition library is used for 
bots to create a transcription of what is said in the microphone to text. With the potential use
of background noise and an API that may not always be available, 
This is out of scope for the project and will not be used because of its unreliability
Code is provided to show that we attempted to add in additional features to the design.
'''

def speech_recognition(recognizer, microphone):

    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source) # attempts to get rid of background noise
        mic_audio = recognizer.listen(source)

    response = {
        "Success": True, "Error": None, "Transcript": None
    }

    try:
        response["Transcript"] = recognizer.recognize_google(mic_audio) #uses Google API
    except sr.RequestError:
        response["Success"] = False
        response["Error"] = "Google API is unavailable"      # cant reach the API
    except sr.UnknownValueError:
        response["Error"] = "Error, unable to recognize speech"        # Could not recognize speech
    return response


recognizer = sr.Recognizer()
mic_input = sr.Microphone(device_index=1)
response = speech_recognition(recognizer, mic_input)

print('\nSuccess: {}'
      '\nErrors: {}'
      '\n\nText from Speech\n{}\n\n{}' \
      .format(response['Success'], response['Error'],'\n\n', response['Transcript']))