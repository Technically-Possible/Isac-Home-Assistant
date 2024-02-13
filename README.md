# Isac-Home-Assistant

This is a Python script that acts as a voice assistant, capable of performing various tasks such as retrieving weather information, setting timers, and providing the current time.

## Prerequisites

Before running the script, make sure you have the following dependencies installed:

- `speech_recognition` library: Used for speech recognition functionality.
- `requests` library: Used for sending HTTP requests to the weather API and a webhook URL.
- `json` library: Used for handling JSON data.
- `re` library: Used for regular expression matching.

You can install these dependencies using `pip`:

pip install speechrecognition requests


## Usage

To use the voice assistant, follow these steps:

1. Set up a weather API: Replace the `weather_api_url` variable with the URL of your preferred weather API endpoint. Make sure you pass the correct parameters for location to retrieve the weather information for the desired location.

2. Set up a webhook URL: Replace the `webhook_url` variable with the URL of your webhook endpoint. The script will send the assistant's responses to this URL.

3. Run the script: Execute the script in your Python environment. The script will continuously listen for a key phrase ("Hey Isaac", "Isaac", or "Hello, Isaac"). When it detects the key phrase, it will prompt you to speak a command. You can give commands like "What's the weather", "Tell me the time", "Start a timer for 5 minutes", or "Check the timer".

4. Interact with the assistant: Speak your command after the prompt. The assistant will recognize your speech, process the command, and provide a response. The response will be displayed in the console, and it will also be sent to the specified webhook URL if provided.

Note: The assistant uses the Google Speech Recognition API for speech recognition. Make sure you have an internet connection for the speech recognition functionality to work.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to modify and adapt the code to suit your needs. Contributions are also welcome!

## Acknowledgements

This script was created using the [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) library for speech recognition and the [Requests](https://pypi.org/project/requests/) library for making HTTP requests.
