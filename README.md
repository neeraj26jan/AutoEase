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

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/autoease.git
2. Navigate to the project directory:
   ```bash
   cd autoease
3. Run the application:
   ```bash
   python autoease.py

## Usage

1. Import the necessary libraries and create an instance of the `AutoEase` class:
   ```python
   from automate import AutoEase
   import time
   import webbrowser
2. Open the web browser (in this case, Google) using the webbrowser module:
   ```python
   webbrowser.open('https://www.google.com')
   time.sleep(3)  # Wait for the browser to load
3. Create an instance of ` AutoEase `:
   ```python
   autoease = AutoEase()
4. Find UI elements based on image recognition with a minimum confidence level (e.g., finding the search box on Google):
   ```python
   elements = autoease.find_elements('search.jpg', min_confidence=0.8)
5. Type text into the found element (e.g., entering "Hello World!" in the Google search box):
   ```python
   autoease.type_at(elements[0], 'Hello World!')
6. Find the "Google Search" button based on another image and simulate a click:
   ```python
   elements = autoease.find_elements('google_search.jpg', min_confidence=0.8)
   autoease.click_at(elements[0])

## Complete Example:

```python
from automate import AutoEase
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

If you want to open browser in ` Incognito Mode ` then replace with these existing code lines in step No. 2:

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
