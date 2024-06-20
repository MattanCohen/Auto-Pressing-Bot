from pywinauto import Application
import json
import os
import time


def print_log(message):
    print(f"$ Window Identifier Bot: --> {message}")
    time.sleep(1)


def print_warning(message):
    print(f"! Window Identifier Bot Warning --> {message}")
    time.sleep(1)


def load_settings(file_path):
    if not os.path.exists(file_path):
        print_warning(f"Settings file does not exist at path {file_path}!")
        return None

    with open(file_path, "r") as file:
        data = json.load(file)

    window_name = data.get("window_name", None)
    print_log(f"Received window name: {window_name}")

    return window_name


window_name = load_settings("../settings.json")

print_log(f'Attempting to bring the window "{window_name}" to the foreground:')

app, application = None, None

try:
    app = Application().connect(title=window_name, timeout=10)
except Exception as e:
    print_warning(f'FAILED TO FIND THE WINDOW "{window_name}" - {str(e)}')

if app is not None:
    application = app.window(title=window_name)
    try:
        application.set_focus()
        print_log(f"\tSUCCESS")
        print_log(f"\tThe window {window_name} has been brought to the foreground.")
        print_warning(
            f"\t It is recommended to minimize the window before attempting to use this bot."
        )
    except Exception as e:
        print_warning(f"Failed to bring the window to the foreground - {str(e)}")
