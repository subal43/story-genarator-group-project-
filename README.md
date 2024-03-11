 Random Story Generator

 Introduction :

The Random Story Generator is a fun little project we created in Python. It's a neat application that generates random stories based on different story parts. we used PySimpleGUI for the GUI and pyttsx3 for text-to-speech conversion.

 Features

- Generates stories with various elements like when, who, residence, went, and happened.
- Displays the generated story in a text area.
- Lets us listen to the story through a button in the GUI.
- Offers a visually appealing and professional-looking interface.

 Requirements

- Python 3.x
- PySimpleGUI
- pyttsx3


Installation

To run the Random Story Generator, we first had to install Python from the official website. Then, we used pip to install PySimpleGUI and pyttsx3:

pip install PySimpleGUI pyttsx3



Usage

1. We simply run the Python script `random_story_generator.py`.
2. The application opens a window titled "Story Generator".
3. We can click the "Generate Random Story" button to generate a new story, which appears in the text area.
4. If we feel like listening to the story instead, we click the "Speak Story" button, and the application speaks the story aloud.




Code Documentation

 `speak(text)`

- This function converts text to speech using pyttsx3.
- I provide the text I want to hear as an argument, and the function speaks it out loud.

`generate_random_story()`

- This function generates a random story using predefined story parts.
- It returns a string containing the generated random story.


`wish()`

- This function greets me based on the time of day.
- It figures out whether it's morning, afternoon, or evening, and greets me accordingly.

`main()`
- The main function creates the GUI window and handles user interactions.
- It consists of a title, a text area to display the generated story, buttons to generate and speak the story, and a footer text.
- The function listens for events such as button clicks and updates the GUI accordingly.
- When we click the "Generate Random Story" button, it generates a new story using the `generate_random_story()` function and updates the text area.
- If we prefer to listen to the story, I click the "Speak Story" button, and the application speaks the story using the `speak()` function.

 
Conclusion
Creating the Random Story Generator was a fun project for us. It allowed us to explore GUI development with PySimpleGUI and text-to-speech conversion with pyttsx3.We can definitely see ourself adding more features and customization options to this project in the future.
