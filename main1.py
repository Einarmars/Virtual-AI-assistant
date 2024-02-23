import speech_recognition as sr
import datetime
import subprocess
import pywhatkit
import webbrowser
import requests

def say(text):
    subprocess.call(['say', text])

recognizer = sr.Recognizer()
say("System ready master")

def send_to_chatgpt(prompt):
    api_key = "YOUR OWN API KEY"
    response = requests.post(
        "https://api.openai.com/v1/completions",
        headers={"Authorization": f"Bearer {api_key}"},
        json={
            "model": "text-davinci-003",
            "prompt": prompt,
            "temperature": 0.5,
            "max_tokens": 100
        },
    )
    return response.json()["choices"][0]["text"].strip()

def cmd():
    while True:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            print("All system running what is your command")
            audio = recognizer.listen(source)
            try:
                command = recognizer.recognize_google(audio, language='en_US').lower()
                print('Command received:', command)
                process_command(command)
            except sr.UnknownValueError:
                say("Sorry, I didn't catch that." + command)
            except sr.RequestError as e:
                say("Sorry, I couldn't reach Google's servers.")

def process_command(command):
    # Implement command handling here
    if 'chrome' in command:
        say('Opening Chrome..')
        subprocess.Popen(['open', '-a', 'Google Chrome'])
    elif 'time' in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        print(current_time)
        say('The current time is ' + current_time)
    elif 'play' in command:
        say('Opening YouTube to play ' + command)
        pywhatkit.playonyt(command)
    elif 'youtube' in command:
        say('Opening YouTube')
        webbrowser.open('http://www.youtube.com')
    elif 'hello' in command:
        say('Greetings all mortals')
    elif 'computer' in command:
        query = command.replace('chatgpt', '', 1).strip()
        if query:
            response = send_to_chatgpt(query)
            print('ChatGPT:', response)
            say(response)
    elif 'love you' in command:
        say('I love you too')
    elif 'open' in command:
        app_name = command.split('open')[1].strip()
        subprocess.Popen(['open', '-a', app_name])
    elif 'search' in command:
        url = command.split('search', 1)[1].strip()
        search_url = f"https://www.google.com/search?q={url}"
        subprocess.Popen(['open', '-a', 'Google Chrome', search_url])
    elif 'thunder' in command:
        say('lightning sir')
    elif 'talk' in command:
        say('Hello, I am your personal assistant and can help you with everyday things on your computer')
    elif 'senior' in command:
        say('That is spanish I would prefer you to talk English with me')
    
        

    elif 'stop' in command:
        say('Shutting down')
        exit()
    

if __name__ == "__main__":
    cmd()
