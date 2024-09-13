# AutoEase

**AutoEase** is a Python-based application designed to automate and simulate mouse and keyboard events. It enables users to perform repetitive tasks with ease by capturing specific screen areas and executing pre-defined actions such as clicks, typing, or navigation. Whether you're automating browser interactions, form filling, or simulating user input, **AutoEase** enhances productivity by streamlining tasks and reducing manual effort. Its intuitive functionality allows users to capture elements of the screen and use them for precise, automated actions in future workflows.

## Features

- **Automated Mouse Events**: Simulate precise mouse movements, clicks, and drags on any captured screen area or browser window.
  
- **Automated Keyboard Input**: Type text into input fields or interact with applications by automating keyboard strokes.

- **Screen Area Capture**: Easily capture specific areas of your screen as image references, and use them to trigger automated events.

- **Image-based Element Detection**: Use image recognition to find UI elements on the screen and interact with them, ensuring accuracy in automation.

- **Customizable Event Sequences**: Define and execute complex sequences of mouse and keyboard actions, tailored to your specific needs.

- **Incognito Mode Support**: Launch browser windows in incognito mode for private automation tasks.

- **Flexible Timing**: Adjust delays and timings between actions to create realistic or accelerated automation flows.

- **User-Friendly Integration**: Seamlessly integrate **AutoEase** into your existing Python workflows for efficient automation.


## Ideal For

- **Developers and Testers**: Automate repetitive tasks, UI testing, and browser interactions with ease, saving time on manual testing and development workflows.

- **Content Creators**: Streamline tasks such as form filling, web navigation, and data entry for creating smooth, hands-free demos and tutorials.

- **Data Entry Professionals**: Automate data input processes for faster and more efficient work without sacrificing accuracy.

- **Researchers and Analysts**: Simplify repetitive tasks, such as gathering data from web sources or automating interactions in research tools and applications.

- **Gamers**: Set up complex in-game automation sequences to enhance gameplay and improve multitasking.

- **IT Administrators**: Automate routine system tasks and processes, making server management or client-side automation effortless.

- **Productivity Enthusiasts**: Reduce the manual effort involved in day-to-day repetitive tasks by automating workflows with minimal setup.


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
   git clone https://github.com/neeraj26jan/autoease.git
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
