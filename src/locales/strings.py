"""
Contains all strings used in the project. Python files displaying text derive from this file.
"""

import os
import json

from src import main

'''
Global
'''

languages = ["en-EN", "cs-CZ"]  # Supported languages

# Map locale values to the BCP 47 standard format
locale_mapping = {
    "Czech_Czechia": "cs-CZ",
}


def get_strings():
    file = main.root_dir + "/src/locales/strings.json"

    with open(os.path.abspath(file), 'r', encoding="utf-8") as file:
        data = json.load(file)
    if main.language in languages:
        data = data.get(main.language)
    else:
        data = data.get("en-EN")

    return data


'''
Welcome Window
'''

welcome = ""
welcome_description = ""
get_started = ""
