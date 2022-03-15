import os, subprocess, speech_recognition as sr
r = sr.Recognizer()
mic = sr.Microphone(device_index=1)
# debug step to print list of possible inputs
#print(mic.list_microphone_names())

while True:
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        text = r.recognize_google(audio)
        if text == 'open Steam':
            print('Understood, opening Steam...')
            subprocess.Popen('D:\\Steam\\Steam.exe')
        if text in ['hey Friday', 'Friday']:
            print('Hello, Jeezy!, what can I help you with?')
        elif text == 'exit':
            print('Understood. Exiting...')
            exit(0)
        else:
            print(f'I could not find an action or response for "{text}"')






