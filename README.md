# Python Virtual Assistant

## Description

Python Virtual Assistant is a voice-activated assistant that can perform various tasks such as telling the time and date, sending emails, sending WhatsApp messages, searching on Google and Youtube, fetching news, telling jokes, and more. It is designed to interact with users through voice commands.

## Prerequisites

- Python 3.x
- `pyttsx3` for text-to-speech conversion
- `datetime` for date and time operations
- `smtplib` for sending emails
- `SpeechRecognition` for recognizing voice commands
- `email` for constructing email messages
- `pyautogui` for interacting with WhatsApp web
- `webbrowser` for opening web pages
- `wikipedia` for fetching information from Wikipedia
- `pywhatkit` for YouTube searches
- `newsapi` for fetching news
- `pyjokes` for jokes
- `requests` for making API requests
- `nltk` for tokenizing words

## Installation

Install the required packages using pip:

```bash
pip install pyttsx3 SpeechRecognition pyautogui wikipedia pywhatkit newsapi-python pyjokes requests nltk
```

## Usage

1. Clone or download this repository.
2. Run the `virtual_assistant.py` script.
3. Interact with the assistant using voice commands.

## Features

### Voice Commands

- **Time**: Asks for the current time.
- **Date**: Asks for the current date.
- **Email**: Sends an email to a predefined contact.
- **Message**: Sends a WhatsApp message to a predefined contact.
- **Wikipedia**: Searches for information on Wikipedia.
- **Google**: Searches for information on Google.
- **YouTube**: Plays a video on YouTube.
- **News**: Fetches the latest news.
- **Weather**: Fetches the weather information for a specified city.
- **Remember**: Stores a piece of information to be remembered.
- **Do I have something**: Retrieves stored information.
- **Instagram**: Opens Instagram.
- **Joke**: Tells a joke.
- **Offline**: Exits the assistant.

## Examples

### Sending an Email

1. Say "email".
2. Specify the recipient (e.g., "Send an email to Mom").
3. Specify the subject.
4. Specify the content of the email.

### Sending a WhatsApp Message

1. Say "message".
2. Specify the recipient (e.g., "Send a message to Dad").
3. Specify the content of the message.

### Searching on Wikipedia

1. Say "Wikipedia".
2. Specify the search term (e.g., "Tell me about Python programming").

---
