# Overview
This bot automates the process of sending key presses to specified applications running in the background. It is designed to assist users in automating repetitive keyboard tasks without the need for direct interaction. The bot operates based on settings defined in a JSON file, allowing for customization of the target window and keys to be pressed.

# Prepare Your PC To Work With The Bot

## Download Necessary Requirements
To ensure that your PC has all the necessary components to run the bot, use the "[Tools/download-all-requirements.bat](Tools/download-all-requirements.bat)" file located in the Tools folder.

# How To Change Settings

## Printing Bot For The Names Of All Windows
### Explanation
This utility helps you identify all currently open windows on your system. It is useful for determining the exact title of the window you wish to target with the auto-pressing bot.

### How To Find Your Window In All Windows 
Run the bat file at path "[Tools/print-all-open-windows.bat](Tools/print-all-open-windows.bat)" to list all open windows. This will help you identify the name of the window you want to target. To validate your choice, use "[Tools/window-identifier-by-name.bat](Tools/window-identifier-by-name.bat)". This script brings the specified window to the foreground, allowing you to confirm its identity.

## Auto Pressing Bot With Your Application
### Setting The Window Name
After identifying the correct window, update the "window_name" in the [settings.json](settings.json) file to match.

### Setting The Keys
Insert any key you wish to be automatically pressed into the "keys" array within the [settings.json](settings.json) file. For a full list of supported keys, click [here](https://pywinauto.readthedocs.io/en/latest/code/pywinauto.keyboard.html) or refer to the file "key-list.txt" located in the .dev directory.

### Changing Debug
To enable system logs, set the "debug" flag to 1 in the [settings.json](settings.json) file. Note that errors will always be printed, regardless of this setting.

### Example
```json
{
    "window_name": "YOUR_WINDOW",
    "keys": [
        "key1",
        "key2"
    ],
    "debug": "0"
}
```

# How To Start The Bot With start-bot.bat File
To start the bot, run the "[start-bot.bat](start-bot.bat)" file. Enjoy automated key pressing! Press "q" to quit the bot at any time.
