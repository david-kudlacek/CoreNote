"""
Contains all strings used in the project. Python files displaying text derive from this file.
"""

import os
import json

'''
Global
'''

languages = ["en-EN", "cs-CZ"]  # Supported languages

# Map locale values to the BCP 47 standard format
locale_mapping = {
    "Czech_Czechia": "cs-CZ",
}




def get_strings(language):
    # Get the current locale settings according to standard (ex. en-EN)
    current_locale = locale.getlocale()
    current_language = strings.locale_mapping.get(current_locale[0], current_locale[0])

    # Move up three directories
    root_dir = os.path.abspath(os.path.join(os.getcwd(), *[".."] * 3))
    file = root_directory + "/src/locales/strings.json"

    with open(os.path.abspath(file), 'r', encoding="utf-8") as file:
        data = json.load(file)
    if language in languages:
        data = data.get(language)
    else:
        data = data.get("en-EN")

    # Welcome dialog
    if True:
        welcome = data["WELCOME"]


'''
Welcome Window
'''

welcome = ""
welcome_description = ""
get_started = ""
