import speech_recognition as sr
from datetime import datetime, timedelta
import requests
import json
import re

# Initialize the speech recognition engine
r = sr.Recognizer()

# Global variables for timer functionality
timer_active = False
timer_end_time = None

# Function to listen for the key phrase
def listen_for_key_phrase():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        phrase = r.recognize_google(audio)
        print("You said:", phrase)
        return phrase
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand you.")
    except sr.RequestError as e:
        print("Sorry, the speech recognition service is unavailable. Error:", str(e))

    return ""

# Function to get the weather information
def get_weather():
    # Replace with your preferred weather API endpoint
    weather_api_url = "https://api.example.com/weather"

    # Replace with the user's location or use a default location
    location = "New York"

    # Send a request to the weather API
    response = requests.get(weather_api_url, params={"location": location})

    if response.status_code == 200:
        weather_data = response.json()
        temperature = weather_data["temperature"]
        weather_description = weather_data["description"]
        return f"The weather in {location} is {temperature} degrees Celsius. {weather_description}"
    else:
        return "Sorry, I couldn't retrieve the weather information."

# Function to start a timer
def start_timer(duration):
    global timer_active, timer_end_time
    timer_active = True
    timer_end_time = datetime.now() + timedelta(minutes=duration)
    print(f"Timer started for {duration} minutes.")

# Function to check the timer status
def check_timer_status():
    global timer_active, timer_end_time
    if timer_active:
        if datetime.now() >= timer_end_time:
            print("Timer ended.")
            timer_active = False
            timer_end_time = None
            return "The timer has ended."
        else:
            remaining_time = timer_end_time - datetime.now()
            minutes = int(remaining_time.total_seconds() // 60)
            seconds = int(remaining_time.total_seconds() % 60)
            return f"The timer is still running. Time remaining: {minutes} minutes and {seconds} seconds."
    else:
        return "No active timer."

# Function to respond based on the key phrase
def respond_to_key_phrase(phrase):
    command_match = re.search(r"(?i)(?:hey isaac|isaac|hello, isaac)[\s,]*(.*)", phrase)
    if command_match:
        command = command_match.group(1).strip().lower()

        if command == "what's the weather":
            response = get_weather()
        elif command in ["what's the time", "tell me the time", "do you have the time"]:
            current_time = datetime.now().strftime("%I:%M %p")
            response = f"The current time is {current_time}."
        elif command.startswith("start a timer for"):
            duration = int(command.split("timer for")[1].strip().split("minutes")[0])
            start_timer(duration)
            response = f"Timer started for {duration} minutes."
        elif command == "check the timer":
            response = check_timer_status()
        else:
            response = "I'm sorry, I cannot perform that command."

        print("Isaac:", response)

        # Send response to the webhook URL
        webhook_url = ""
        payload = {
            "webhook_id": "IsaacWebHook",
            "message": response
        }
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.post(webhook_url, json=payload, headers=headers)

        print("Webhook response status code:", response.status_code)

# Main program loop
while True:
    user_input = listen_for_key_phrase()
    respond_to_key_phrase(user_input)
