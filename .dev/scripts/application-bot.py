from pywinauto import Application
import json
import os
import time

# Global debug flag
debug = None


def print_warning(message):
    print(f"! Auto Pressing Bot Warning --> {message}")


def print_log(message):
    global debug
    if debug:
        print(f"$ Auto Pressing Bot Log: --> {message}")


def load_settings(file_path):
    global debug

    # Open file
    if not os.path.exists(file_path):
        print_warning(
            f"Settings file does not exist at path {file_path}! Check the README file for more info."
        )
        return None, None, None

    with open(file_path, "r") as file:
        data = json.load(file)

    # Debug
    debug_flag = data.get("debug", "").lower()
    debug = debug_flag == "1"

    print_log(f"Debug mode ---> ACTIVATED!")
    print_log(
        f"Starting the bot with debug logs. To stop printing, read the README file"
    )

    # Window name
    window_name = data.get("window_name", None)
    if window_name is not None:
        print_log(f"Received window name: {window_name}")
    else:
        print_warning(
            f"window_name is not specified in the settings file! Check the README file for more info."
        )

    # Keys
    keys = data.get("keys", None)
    if keys is not None:
        print_log(f"Received keys array: {keys}")
    else:
        print_warning(
            f"keys array is empty in the settings file. check the README file for more info."
        )

    # Keys
    press_delay_in_seconds = float(data.get("press_delay_in_seconds", 0.1))
    print_log(f"Received this press delay in seconds: {press_delay_in_seconds}")

    # Return
    return window_name, keys, press_delay_in_seconds, debug


window_name, keys, press_delay_in_seconds, debug = load_settings("settings.json")

app, application = None, None

try:
    app = Application().connect(title=window_name, timeout=10)
except Exception:
    print_warning(f'FAILED TO FIND THE WINDOW "{window_name}"')

if app is not None:
    application = app.window(title=window_name)


def press_keys_in_bluestacks_background(keys=[]):
    if keys is [] or None:
        print_warning("Keys array is empty. Read the README file for more info.")
        return

    for key in keys:
        try:
            print_log(f"Pressing the key {key} on the window {window_name}")
            application.send_keystrokes(key)
            print_log(f"Key pressed.")
        except Exception as e:
            print_warning(f"Exception! - {e}")

        time.sleep(press_delay_in_seconds)


if application is not None:
    print("------------------------------------------------")
    print("Starting the bot. To stop it, close the window.")
    print("------------------------------------------------")

    print_log("Starting to press the keys on the window.")

    while True:
        press_keys_in_bluestacks_background(keys)
