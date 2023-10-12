import json
import os
import locale

from src.locales import strings
from src.windows.welcome_window import welcome

version = "0.0.1-alpha"

settings_name = "settings.json"
root_dir = os.path.abspath(os.path.join(os.getcwd(), *[".."]))


def init_data():
    # current_locale = locale.getlocale()
    # current_language = strings.locale_mapping.get(current_locale[0], "en-EN")

    init_json()


def init_json():
    # Default JSON values
    def_data = {
        "version": version,
        "language": "en-EN",
    }

    if not os.path.exists(settings_name):
        # Open the file in write mode and write the JSON data
        with open(settings_name, "w") as json_file:
            json.dump(def_data, json_file, indent=4)


def get_language():
    with open(settings_name, "r") as file:
        data = json.load(file)
        language = data["language"]
    return language


def change_language(new_language):
    with open(settings_name, "r") as json_file:
        data = json.load(json_file)
    if new_language == "English":
        data["language"] = "en-En"
    elif new_language == "Čeština":
        data["language"] = "cs-CZ"

    # Write the updated data back to the JSON file
    with open(settings_name, "w") as json_file:
        json.dump(data, json_file, indent=4)


if __name__ == "__main__":
    init_data()

    welcome.construct()
