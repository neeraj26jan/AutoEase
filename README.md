# AutoEase

**AutoEase** is an intuitive and powerful automated keyboard and mouse software designed to streamline your workflows and enhance productivity. Whether you're performing repetitive tasks, automating clicks, or simulating complex keyboard sequences, AutoEase handles it all with precision and ease.

## Features

- **Seamless Automation**: Automate keyboard inputs and mouse actions with ease.
- **Customizable Macros**: Set up complex or repetitive tasks using customizable macros.
- **Realistic Mouse Movements**: Simulate human-like mouse movements and clicks.
- **User-Friendly Interface**: Simple and intuitive interface for easy setup and operation.
- **Multi-App Automation**: Automate across multiple apps with task scheduling.

## Ideal for

- **Professionals**: Save time on daily repetitive tasks.
- **Gamers**: Automate in-game actions for enhanced performance.
- **General Users**: Simplify workflows and boost productivity with automated actions.

## Dependencies
* pyautogui
* opencv-python
* pyclick
* numpy
* asyncio
* pynput

We can install these all by giving command: <br />
` pip install pyautogui opencv-python pyclick numpy asyncio pynput `

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/autoease.git
2. Navigate to the project directory:
   ```bash
   cd autoease
3. Run the application:
   ```bash
   python launch.py

## Usage

1. First, we need to capture the area, part, or element of the screen or browser window where we want to perform the mouse or keyboard event. To achieve this, we will run the ` take_ss.py ` file, and after selecting the specific area with the mouse, we will save it as a JPEG image file inside the project's root directory. These image files will later be used in our executable script, ` launch.py `.
2. Import the necessary libraries and create an instance of the `AutoEase` class:
   ```python
   from autoease import AutoEase
   import time
   import webbrowser
3. Open the web browser (in this case, Google) using the webbrowser module:
   ```python
   webbrowser.open('https://www.google.com')
   time.sleep(3)  # Wait for the browser to load
4. Create an instance of ` AutoEase `:
   ```python
   autoease = AutoEase()
5. Find UI elements based on image recognition with a minimum confidence level (e.g., finding the search box on Google):
   ```python
   elements = autoease.find_elements('search.jpg', min_confidence=0.8)
6. Type text into the found element (e.g., entering "Hello World!" in the Google search box):
   ```python
   autoease.type_at(elements[0], 'Hello World!')
7. Find the "Google Search" button based on another image and simulate a click:
   ```python
   elements = autoease.find_elements('google_search.jpg', min_confidence=0.8)
   autoease.click_at(elements[0])

## Complete Example:

```python
from autoease import AutoEase
import time
import webbrowser

# Open the web browser
webbrowser.open('https://www.google.com')

# Wait for the browser to open
time.sleep(3)

autoease = AutoEase()

# Find search box and type "Hello World!"
elements = autoease.find_elements('search.jpg', min_confidence=0.8)
autoease.type_at(elements[0], 'Hello World!')

# Find Google Search button and click it
elements = autoease.find_elements('google_search.jpg', min_confidence=0.8)
autoease.click_at(elements[0])
```

## Incognito Mode:

If you want to open the browser in Incognito Mode, replace the existing code lines with the following in Step No. 3.:

```python
import subprocess
import sys

def open_chrome_incognito(url):
    if sys.platform == "win32":
        subprocess.Popen(['start', 'chrome', '--incognito', url], shell=True)
    elif sys.platform == "darwin":  # macOS
        subprocess.Popen(['open', '-a', 'Google Chrome', '--args', '--incognito', url])
    else:  # Linux
        subprocess.Popen(['google-chrome', '--incognito', url])

# Open the web browser in Incognito Mode
open_chrome_incognito('https://www.google.com')

# Wait for the browser to open
time.sleep(3)  # Wait for the browser to load
```
