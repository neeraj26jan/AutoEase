import cv2
import numpy as np
import pyautogui
import tkinter as tk
from tkinter import simpledialog, messagebox
from pynput import keyboard
import threading
import sys
import traceback

# Global variables
start_x, start_y, end_x, end_y = 0, 0, 0, 0
drawing = False
enable_selection = False
exit_event = threading.Event()

def draw_rectangle(event, x, y, flags, param):
    global start_x, start_y, end_x, end_y, drawing

    if enable_selection:
        if event == cv2.EVENT_LBUTTONDOWN:
            drawing = True
            start_x, start_y = x, y

        elif event == cv2.EVENT_MOUSEMOVE:
            if drawing:
                end_x, end_y = x, y

        elif event == cv2.EVENT_LBUTTONUP:
            drawing = False
            end_x, end_y = x, y

def start_selection():
    global enable_selection, start_x, start_y, end_x, end_y, exit_event
    enable_selection = True

    # Capture a full-screen screenshot
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    cv2.namedWindow("Select Area", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Select Area", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.setMouseCallback("Select Area", draw_rectangle)

    while not exit_event.is_set():
        img = screenshot.copy()
        if enable_selection and (start_x != end_x and start_y != end_y):
            cv2.rectangle(img, (start_x, start_y), (end_x, end_y), (0, 255, 0), 2)

        cv2.imshow("Select Area", img)

        key = cv2.waitKey(1) & 0xFF
        if key == 13:  # Enter key
            break
        if key == 27:  # Escape key
            exit_event.set()
            print("Program exited by user.")
            break

    cv2.destroyAllWindows()

    if not exit_event.is_set() and start_x < end_x and start_y < end_y:
        prompt_for_filename(screenshot)
    else:
        print("Invalid selection or exit by user. No file saved.")

def prompt_for_filename(screenshot):
    # Initialize Tkinter for the prompt
    prompt_root = tk.Tk()
    prompt_root.withdraw()  # Hide the root window

    try:
        # Ask user for the file name
        file_name = simpledialog.askstring("Input", "Enter the name of the file (without extension):", parent=prompt_root)
        if not file_name:
            file_name = "selected_area"

        # Calculate the region of interest (ROI)
        roi = screenshot[start_y:end_y, start_x:end_x]

        # Save the ROI as a JPEG file
        file_path = f"{file_name}.jpg"
        cv2.imwrite(file_path, roi)
        print(f"Selected area saved as {file_path}")

    except Exception as e:
        print(f"Error while saving file: {e}")
    finally:
        # Destroy the Tkinter prompt window
        prompt_root.destroy()

def on_activate():
    start_selection()

def on_press(key):
    try:
        if key == keyboard.Key.esc:
            exit_event.set()
            print("Program exited by user.")
            return False  # Stop the listener
    except Exception as e:
        print(f"Error in on_press: {e}")

def setup_hotkey_listener():
    try:
        with keyboard.GlobalHotKeys({
                '<ctrl>+<shift>+s': on_activate}) as h:
            h.join()
    except Exception as e:
        print(f"Error in hotkey listener: {e}")

def setup_exit_listener():
    try:
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()
    except Exception as e:
        print(f"Error in exit listener: {e}")

def clean_up():
    print("Cleaning up resources...")
    cv2.destroyAllWindows()
    sys.exit()

def main():
    global exit_event

    # Initialize Tkinter in the main thread
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    try:
        # Show instructions to the user
        messagebox.showinfo("Instructions", "Switch to the desired window, then press 'Ctrl+Shift+S' to start selection, click and drag to select the area on the screen, and press 'Enter' to save and quit. Press 'Escape' to exit the program without saving.", parent=root)

        # Run the hotkey listener for selection in a separate thread
        hotkey_listener_thread = threading.Thread(target=setup_hotkey_listener, daemon=True)
        hotkey_listener_thread.start()

        # Run the exit listener in a separate thread
        exit_listener_thread = threading.Thread(target=setup_exit_listener, daemon=True)
        exit_listener_thread.start()

        # Keep the main thread running
        while not exit_event.is_set():
            root.update()

    except Exception as e:
        print(f"Error: {e}")
        traceback.print_exc()

    finally:
        clean_up()

if __name__ == "__main__":
    main()
