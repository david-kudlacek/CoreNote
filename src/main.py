import json
import os

from src.locales import strings
from src.windows.welcome_window import welcome

version = "0.0.1-alpha"

data_file = "data.json"
default_application_data = {
    "version": version,
    "language": "en"
}
root_directory = os.path.abspath(os.path.join(os.getcwd(), *[".."]))


def init_data():
    with open(data_file, "w") as json_file:
        json.dump(default_application_data, json_file, indent=4)


def write_data(data):
    with open(data_file, "w") as file:
        json.dump(data, file, indent=4)


def get_data():
    with open(data_file, 'r') as file:
        application_data = json.load(file)

    return application_data


if __name__ == "__main__":
    if not os.path.exists(data_file):
        init_data()

    welcome.construct()
