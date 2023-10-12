import json
import os
import locale

from locales import strings
from src.windows.welcome_window import welcome

version = "0.0.1-alpha"
file_name = "settings.json"
root_dir = os.path.abspath(os.path.join(os.getcwd(), *[".."]))


def init_data():
    # Get the current locale settings according to standard (ex. en-EN)
    current_locale = locale.getlocale()
    current_language = strings.locale_mapping.get(current_locale[0], current_locale[0])

    init_json(current_language)


def init_json(lang):
    # Default JSON values
    def_data = {
        "version": version,
        "language": lang,
    }

    if os.path.exists(file_name):
        pass
    else:
        # Open the file in write mode and write the JSON data
        with open(file_name, "w") as json_file:
            json.dump(def_data, json_file, indent=4)


if __name__ == "__main__":
    init_data()

    with open(file_name, "r") as file:
        data = json.load(file)
        language = data["language"]

    welcome.construct()
