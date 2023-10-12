import json
import os
import locale

from locales import strings
from src.windows.welcome_window import welcome


def init_data():
    # Get the current locale settings according to standard (ex. en-EN)
    current_locale = locale.getlocale()
    current_language = strings.locale_mapping.get(current_locale[0], current_locale[0])

    # Initialize strings for current language
    strings.init_strings(current_language, os.getcwd() + "/locales/strings.json")


def init_json():
    # Default JSON values
    data = {
        "version": "0.0.1-alpha",
        "language": "en-EN",
    }

    file_name = "settings.json"

    if os.path.exists(file_name):
        # Open the JSON file in read mode and load the data
        with open(file_name, "r") as file:
            data = json.load(file)
    else:
        # Open the file in write mode and write the JSON data
        with open(file_name, "w") as file:
            json.dump(data, file, indent=4)


if __name__ == "__main__":
    init_json()
    init_data()

    welcome.construct()
