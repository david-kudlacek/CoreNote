"""
Handles all critical data and functions.
Starts the application.
"""

import os
import sys
import json

from src.windows.welcome_window import welcome
from src.windows.main_window import central

version = "0.0.1-alpha"
root_directory = os.getcwd()[:os.getcwd().find("CoreNote")]
default_data = {
    "VERSION": version,
    "LANGUAGE": "en",
    "FIRST_RUN": True
}


def find_file(target_file):
    for root, dirs, files in os.walk(root_directory):
        if target_file in files:
            file_path = os.path.join(root, target_file)
            return file_path
    return None


def init_data():
    with open("data.json", "w") as file:
        json.dump(default_data, file, indent=4)


def write_data(data):
    with open(data_file, "w") as file:
        json.dump(data, file, indent=4)


def get_data():
    with open(data_file, 'r') as file:
        application_data = json.load(file)

    return application_data


# RETRIEVE JSON FILE PATHS
data_file = find_file("data.json")
string_file = find_file("strings.json")
style_file = find_file("styles.json")


if __name__ == "__main__":
    if data_file is None:
        init_data()
        os.execv(sys.executable, ['python'] + sys.argv)

    if get_data()["FIRST_RUN"]:
        welcome.construct()
    else:
        central.construct()
