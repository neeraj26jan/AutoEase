# AutoEase

**AutoEase** is an application written with Python that is meant to automate or simulate mouse and keyboard clicks. It does this by allowing the user to carry out repetitive tasks with ease such as clicking, typing in or navigating certain predefined screen areas where certain predefined actions are executed. It doesn’t matter whether you want to simulate a browser and fill out forms, click around, or even add some AutoEase helps with performing such operations by cutting down the workload and letting the user only work on the most relevant issues. It has made it easier for users to capture certain portions of the screen, and these portions can in turn be used appropriately in future workflows requiring some form of automation.

## Features

- **Automated Mouse Events**: Perform mechanical use of the mouse cursor such as movement, clicking, and dragging with the cursor on any image or web page element.
  
- **Automated Keyboard Input**: Type text into input fields or interact with applications by automating keyboard strokes.

- **Screen Area Capture**: Use a reference image created from screen captures to facilitate the occurrence of future predefined operations.

- **Image-based Element Detection**: Perform automation on the elements of the user interface located on the display using the images relevant to a computer program.

- **Customizable Event Sequences**: Design and execute customized series of mouse or keyboard events for performing complex tasks.

- **Incognito Mode Support**: Spare incognito browser windows for execution of the scripts requiring loss of validation.

- **Flexible Timing**: Control how actions are launched in automation making realistic or time-compressed automation flows.

- **User-Friendly Integration**: Integration of AutoEase into existing Python scripts for various purposes where automation is required without any complexity.


## Perfect For

- **Developers and Quality Assurance**: Make repetitive activities such as UI testing and browser activity easier by saving time spent on manual testing and development disciplines.

- **Content Creators**: Simplify some activities, such as filling instruction pages, navigating to web pages, and inputting data to make easier high-quality demos and trainings.

- **Data Entry Experts**: Reduce the time that it would take to perform these data input activities without compromising on quality.

- **Research and Analysis**: Reduce repetitive work such as collecting information from the web or automating the use of research applications.

- **Gamers**: Configure such that specific combinations of complex multi keystroke and mouse click sequences are executed in-game to allow for heightened play and multi tasking.

- **IT Administrators**: Simplify simple administrative tasks and operations to make the work of managing the server or doing client’s side automation very minimal.

- **Productivity Enthusiasts**: When doing repetitive processes in day to day operations of organizations, it is possible to automate and make at least a fraction of the work to be done without loosing so much of the original workflows.

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

1. First, it is essential to determine the area (part or element) of the screen or browser's window where mouse or keyboard event is to occur. For this,” therefore,” we run the take_ss.py file, that allows you to take amp, for example, a mouse pointer and select an area that we will thereafter save such as a JPEG image inside the project’s folder. Those image files will later be used in execution of our script ‘launch.py’.
2. Import the required libraries to create an instance of AutoEase class:
   ```python
   from autoease import AutoEase
   import time
   import webbrowser
3. Use a webbrowser module to launch a web browser for this example 'Google.com':
   ```python
   webbrowser.open('https://www.google.com')
   time.sleep(3)  # Wait for the browser to load
4. Create an instance of ` AutoEase `:
   ```python
   autoease = AutoEase()
5. Locate UI elements using image based approaches with the set minimum confidence level. For example here we will locate the Google search box in an image:
   ```python
   elements = autoease.find_elements('search.jpg', min_confidence=0.8)
6. Insert the provided text on the indicated area (example, "Hello World!" typed on the textbo located at Google search):
   ```python
   autoease.type_at(elements[0], 'Hello World!')
7. Search for Elements for the image “Google Search” and click on the button by simulating the click:
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
