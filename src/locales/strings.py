"""
Contains all strings used in the project. Python files displaying text derive from this file.
"""

import os
import json
from src import main


supported_languages = ["en", "cs"]
locale_mapping = {
    "English": "en",
    "Čeština": "cs"
}


def get_string_data():
    string_file = main.root_directory + "/src/locales/strings.json"

    with open(os.path.abspath(string_file), 'r', encoding="utf-8") as file:
        string_data = json.load(file)
    if get_language() in supported_languages:
        string_data = string_data.get(get_language())
    else:
        string_data = string_data.get("en")

    return string_data


def get_language():
    return main.get_application_data()["language"]


def change_language(new_language):
    data_file = main.root_directory + "/src/data.json"

    with open(data_file, "r") as file:
        data = json.load(file)
    for language in supported_languages:
        if language == new_language:
            data["language"] = new_language
        else:
            data["language"] = "en"

    # Write the updated data back to the JSON file
    with open(data_file, "w") as file:
        json.dump(data, file, indent=4)
