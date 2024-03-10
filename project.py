import random
import datetime
import pyttsx3
import PySimpleGUI as sg

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(text):
    engine.say(text)
    print(text)
    engine.runAndWait()

def generate_random_story():
    when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago', 'On 20th Jan', 'In my childhood', 'During the summer vacation', 'In the distant future', 'Once upon a time']
    who = ['a clever rabbit', 'a wise elephant', 'a curious mouse', 'a slow turtle', 'a mischievous cat', 'a majestic lion', 'a loyal dog', 'a playful monkey', 'a cuddly bear', 'a colorful bird', 'a graceful giraffe', 'a hopping kangaroo', 'a peaceful panda']
    residence = ['Barcelona', 'India', 'Germany', 'Venice', 'England', 'New York', 'Tokyo', 'Paris', 'Sydney', 'Rio de Janeiro', 'Moscow', 'Cairo']
    went = ['cinema', 'university', 'seminar', 'school', 'laundry', 'zoo', 'park', 'beach', 'restaurant', 'hospital', 'library', 'gym', 'market', 'concert']
    happened = ['made a lot of friends', 'ate a delicious burger', 'found a mysterious key', 'solved a challenging mystery', 'wrote an inspiring book', 'learned a new language', 'built a cozy house', 'won a prestigious competition', 'started a successful business', 'adopted a cute pet', 'discovered a hidden treasure', 'traveled around the world', 'met a famous celebrity', 'learned to dance gracefully', 'won a life-changing lottery']

    story_parts = [
        f"{random.choice(when)}, {random.choice(who)} lived in {random.choice(residence)}. One {random.choice(when)}, they decided to visit the {random.choice(went)}. While walking to the {random.choice(went)}, they encountered {random.choice(who)}. They decided to team up and continued their journey...",
        f"At the {random.choice(went)}, they {random.choice(happened)}. The {random.choice(went)} was bustling with activity, and {random.choice(who)} was amazed by the sights and sounds around them. They spent hours exploring and enjoying the {random.choice(went)}. Afterwards, they decided to have a meal at a nearby {random.choice(['restaurant', 'cafe', 'food court'])}...",
        f"After spending some time at the {random.choice(went)}, they decided to explore {random.choice(residence)} further. They stumbled upon a {random.choice(['hidden', 'forgotten', 'enchanted', 'mysterious'])} {random.choice(['forest', 'cave', 'castle', 'ruins'])} and decided to explore it. Inside, they found many {random.choice(['treasures', 'mysteries', 'secrets', 'challenges'])} waiting to be discovered...",
        f"While exploring the {random.choice(['forest', 'cave', 'castle', 'ruins'])}, they encountered {random.choice(who)} who was also exploring the area. Together, they faced many challenges and overcame them with courage and determination. They formed a strong bond and decided to continue their adventures together...",
        f"Eventually, they returned home, tired but happy, with memories that would last a lifetime. They realized that the greatest adventures are the ones shared with friends."
    ]

    story = ' '.join(story_parts)
    return story

def main():

    wish()
    sg.theme('DarkRed2')

    layout = [
        [sg.Text("Random Story Generator", size=(30, 1), font=("Matura MT Script Capitals", 30), justification='center', relief=sg.RELIEF_RIDGE)],
        [sg.Multiline(size=(100, 15), key='-OUTPUT-', font=("Goudy Old Style", 14), autoscroll=True, disabled=True)],
        [sg.Button('Generate Random Story', size=(20, 2), font=("Cooper Black", 16)), sg.Button('Speak Story', size=(20, 2), font=("Cooper Black", 16))],
        [sg.Text("Developed by Tuhin Tamal Subal Somnath and Ankur", size=(50, 1), font=("Forte", 10), justification='center', relief=sg.RELIEF_RIDGE)]
    ]

    window = sg.Window('Story Generator', layout, resizable=True, finalize=True)



    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == 'Generate Random Story':
            story = generate_random_story()
            window['-OUTPUT-'].update(story)
        elif event == 'Speak Story':
            story = window['-OUTPUT-'].get()
            speak(story)

    window.close()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good morning everyone")
    elif hour > 12 and hour < 18:
        speak("Good afternoon everyone")
    else:
        speak("Good evening everyone")
    speak("Hi, I am the Story Generator")
    speak("Let me tell you an interesting story")

if __name__ == "__main__":
    main()
