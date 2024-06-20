from pywinauto import Application
import json
import os
import threading

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
    if not os.path.exists(file_path):
        print_warning(f"Settings file does not exist at path {file_path}!")
        return None, None, None

    with open(file_path, "r") as file:
        data = json.load(file)

    window_name = data.get("window_name", None)
    print_log(f"Received window name: {window_name}")

    keys = data.get("keys", None)
    print_log(f"Received keys array: {keys}")

    debug_flag = data.get("debug", "").lower()
    print_log(f"Received debug flag {debug_flag}")

    debug = debug_flag == "1"

    if debug_flag is not None and debug_flag != "0" and debug_flag != "1":
        print_warning(
            f"Debug flag {debug_flag} is not recognized. Check the README for more information."
        )

    return window_name, keys, debug


window_name, keys, debug = load_settings("settings.json")

print_log("The bot will start with these settings:")
print_log(f"\twindow name: {window_name}")
print_log(f"\tkeys to press: {keys}")
print_log(f"\tdebug value: {debug}")

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

    print_log("Starting to press the keys on the window.")
    for key in keys:
        try:
            application.send_keystrokes(key)
            print_log(f"Pressing the key {key} on the window {window_name}")
        except Exception as e:
            print_warning(f"Exception {e}")


if application is not None:
    print("------------------------------------------------")
    print("Starting the bot. To stop it, close the window.")
    print("------------------------------------------------")

    while True:
        press_keys_in_bluestacks_background(keys)
