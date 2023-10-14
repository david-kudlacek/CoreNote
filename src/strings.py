"""
Manages all strings used in the project and locale settings.
Project files displaying text derive from this file.
Custom and modified Qt style sheets derive from this file.
"""

import json
from src import main


supported_languages = ["en", "cs"]
locale_mapping = {
    "English": "en",
    "Čeština": "cs"
}


def get_style(style):
    with open(main.find_file("styles.json"), 'r') as file:
        data = json.load(file)
    return data[style]


def get_strings():
    string_data = get_data()

    if get_language() in supported_languages:
        string_data = string_data.get(get_language())
    else:
        string_data = string_data.get("en")

    return string_data


def get_data():
    with open(main.find_file("strings.json"), 'r', encoding="utf-8") as file:
        string_data = json.load(file)

    return string_data


def get_language():
    return main.get_data()["language"]


def set_language(new_language):
    application_data = main.get_data()
    for language in supported_languages:
        if language == new_language:
            application_data["language"] = new_language
        else:
            application_data["language"] = "en"

    main.write_data(application_data)
