import time
from pywinauto import Desktop


def print_log(message):
    print(f"$ Window Names Bot: --> {message}")
    time.sleep(0.2)


def print_warning(message):
    print(f"! Window Names Bot Warning --> {message}")
    time.sleep(1)


def list_windows():
    desktop = Desktop(
        backend="uia"
    )  # Use 'uia' or 'win32' depending on the application type

    windows = desktop.windows()
    if not windows:
        print_warning(
            "No windows found. Ensure that there are open windows or check the backend."
        )
        return

    print_log("List of all available windows:")

    for window in windows:
        try:
            title = window.window_text()
            if title != "" and title is not None:
                print_log(f'| Window Name | "{title}"')
        except Exception as e:
            print_warning(f"Failed to retrieve title for a window: {str(e)}")


print_log("--- Starting the window listing bot ---")
list_windows()
print_log("--- Operation completed. Exiting ---")
